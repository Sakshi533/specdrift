"""SpecDrift GRPO training kernel (Kaggle T4). DRAFT — run after problem scale-up.

Expects the repo attached as a Kaggle dataset at /kaggle/input/specdrift-repo
(push with kaggle_train/push_dataset.py). One run does: baseline eval on
held-out problems -> GRPO training on the rest -> post-training eval, writing
results JSONL + LoRA adapter to /kaggle/working.

Training formulation: single-turn teacher-forced episodes. For version k the
prompt replays the conversation with the REFERENCE code for v_{k-1} standing
in for the model's earlier replies, and asks for the v_k update. Reward is the
executable score: 0.6 * current-spec pass rate + 0.4 * (1 - regression rate).
"""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ.setdefault("PYTORCH_ALLOC_CONF", "expandable_segments:True")

REPO = Path("/kaggle/input/specdrift-repo")
if not (REPO / "specdrift" / "schema.py").exists():
    # dir_mode="zip" uploads can nest; locate the package wherever it landed
    for cand in Path("/kaggle/input").rglob("schema.py"):
        if cand.parent.name == "specdrift":
            REPO = cand.parent.parent
            break
WORK = Path("/kaggle/working")
print("[data] repo root:", REPO, "->", sorted(p.name for p in REPO.iterdir()))
sys.path.insert(0, str(REPO))

MODEL = "Qwen/Qwen2.5-Coder-1.5B-Instruct"
EVAL_IDS = ["slugify", "word_wrap", "log_folder", "seat_fill", "bill_split"]  # held out; never trained on
MAX_STEPS = 150  # optimizer steps; 8 completions each. Long prompts -> ~80s/step on T4
NUM_GENERATIONS = 8
MAX_COMPLETION = 768

t0 = time.time()
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "-U", "trl", "peft"], check=True)
subprocess.run([sys.executable, "-m", "pip", "uninstall", "-q", "-y", "torchao"], check=False)

import dataclasses

import torch
from datasets import Dataset
from peft import LoraConfig
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import GRPOConfig, GRPOTrainer

from specdrift.rollout import SYSTEM_PROMPT, extract_code, run_episode
from specdrift.sandbox import run_tests
from specdrift.schema import load_all
from specdrift.scoring import score_version

problems = load_all(REPO / "problems")
train_problems = [p for p in problems if p.id not in EVAL_IDS]
eval_problems = [p for p in problems if p.id in EVAL_IDS]
print(f"[data] {len(train_problems)} train / {len(eval_problems)} eval problems")


def build_samples(probs):
    samples = []
    for p in probs:
        refs = {v.number: v.reference_path.read_text(encoding="utf-8") for v in p.versions}
        for v in p.versions:
            msgs = [{"role": "system", "content": SYSTEM_PROMPT}]
            for prev in p.versions[: v.number - 1]:
                user = prev.spec if prev.number == 1 else \
                    f"Requirement update from the client:\n\n{prev.spec}"
                msgs.append({"role": "user", "content": user})
                msgs.append({"role": "assistant",
                             "content": f"```python\n{refs[prev.number]}\n```"})
            user = v.spec if v.number == 1 else \
                f"Requirement update from the client:\n\n{v.spec}"
            msgs.append({"role": "user", "content": user})
            samples.append({"prompt": msgs, "tests_path": str(v.tests_path),
                            "version": v.number})
    return samples


train_samples = build_samples(train_problems)
print(f"[data] {len(train_samples)} training samples")


def spec_reward(completions, tests_path, version, **kwargs):
    rewards = []
    for completion, tp, ver in zip(completions, tests_path, version):
        text = completion if isinstance(completion, str) else completion[0].get("content", "")
        code = extract_code(text)
        score = score_version(run_tests(code, Path(tp), timeout=10.0), ver)
        rewards.append(score.reward)
    return rewards


def evaluate(model, tokenizer, tag):
    """Multi-turn eval on held-out problems (the model sees its OWN prior replies)."""
    model.eval()

    def generate(messages):
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = tokenizer(text, return_tensors="pt").to(model.device)
        with torch.no_grad():
            out = model.generate(**inputs, max_new_tokens=MAX_COMPLETION, do_sample=False,
                                 pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id)
        return tokenizer.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)

    rows = []
    for p in eval_problems:
        for rec in run_episode(p, generate):
            rows.append({"tag": tag, "problem": p.id, **rec.to_dict()})
        print(f"[eval:{tag}] {p.id}: "
              f"{[(r['version'], round(r['current_pass'] / max(1, r['current_total']), 2)) for r in rows if r['problem'] == p.id]}")
    out_path = WORK / f"eval_{tag}.jsonl"
    out_path.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
    cur = sum(r["current_pass"] for r in rows) / max(1, sum(r["current_total"] for r in rows))
    carried = sum(r["carried_total"] for r in rows)
    reg = 1 - sum(r["carried_pass"] for r in rows) / carried if carried else 0.0
    print(f"[eval:{tag}] AGGREGATE current_pass={cur:.3f} regression={reg:.3f}")
    return cur, reg


tokenizer = AutoTokenizer.from_pretrained(MODEL)
base_model = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.float16, device_map="cuda:0")
before = evaluate(base_model, tokenizer, "before")
del base_model
torch.cuda.empty_cache()

wanted = dict(
    output_dir=str(WORK / "grpo_out"),
    per_device_train_batch_size=NUM_GENERATIONS // 2,
    gradient_accumulation_steps=2,   # generation batch stays = NUM_GENERATIONS
    gradient_checkpointing=True,
    num_generations=NUM_GENERATIONS,
    max_completion_length=MAX_COMPLETION,
    max_steps=MAX_STEPS,
    learning_rate=2e-5,
    logging_steps=5,
    fp16=True,
    report_to="none",
    temperature=0.9,
    save_strategy="no",
)
valid = {f.name for f in dataclasses.fields(GRPOConfig)}
print(f"[setup] dropped GRPOConfig args: {sorted(k for k in wanted if k not in valid)}")
args = GRPOConfig(**{k: v for k, v in wanted.items() if k in valid})

trainer = GRPOTrainer(
    model=MODEL,
    reward_funcs=spec_reward,
    args=args,
    train_dataset=Dataset.from_list(train_samples * 50),  # plenty of epochs; max_steps caps
    peft_config=LoraConfig(r=16, lora_alpha=32, task_type="CAUSAL_LM",
                           target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                                           "gate_proj", "up_proj", "down_proj"]),
)
t1 = time.time()
trainer.train()
print(f"[train] {MAX_STEPS} steps in {(time.time() - t1) / 60:.1f} min")
trainer.model.save_pretrained(str(WORK / "lora_adapter"))

merged = trainer.model.merge_and_unload()
after = evaluate(merged, tokenizer, "after")

print(f"[RESULT] before: current={before[0]:.3f} regression={before[1]:.3f}")
print(f"[RESULT] after:  current={after[0]:.3f} regression={after[1]:.3f}")
print(f"[RESULT] total wall time {(time.time() - t0) / 60:.1f} min")
print("TRAIN OK")
