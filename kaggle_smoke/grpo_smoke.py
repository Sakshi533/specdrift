"""SpecDrift GRPO smoke test — Kaggle T4.

Goal: prove the full RL loop (generate -> execute code -> reward -> GRPO step)
runs on free Kaggle GPU within sane time. NOT meant to show learning gains;
10 steps only. Prints SMOKE OK plus timing if everything works.
"""

import os
import re
import subprocess
import sys
import tempfile
import time

os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # keep it single-GPU simple
os.environ["TOKENIZERS_PARALLELISM"] = "false"

t0 = time.time()
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "-U", "trl", "peft"], check=True)
# Kaggle ships torchao 0.10.0, which new peft rejects; absent is fine, stale is not.
subprocess.run([sys.executable, "-m", "pip", "uninstall", "-q", "-y", "torchao"], check=False)
print(f"[setup] pip done in {time.time() - t0:.0f}s")

import dataclasses

import torch
import trl
from datasets import Dataset
from peft import LoraConfig
from trl import GRPOConfig, GRPOTrainer

print(f"[setup] trl version: {trl.__version__}")
print(f"[setup] gpu: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'NONE'}")

MODEL = "Qwen/Qwen2.5-Coder-0.5B-Instruct"

TASKS = [
    {
        "prompt": [{"role": "user", "content":
            "Write a Python function `merge(a, b)` that merges two ascending-sorted "
            "integer lists into one ascending-sorted list containing all elements. "
            "Reply with a single ```python code block."}],
        "tests": "assert merge([1,3],[2,4]) == [1,2,3,4]\n"
                 "assert merge([],[1]) == [1]\n"
                 "assert merge([1,1],[1]) == [1,1,1]\n",
    },
    {
        "prompt": [{"role": "user", "content":
            "Write a Python function `slugify(s)` that lowercases s, replaces runs of "
            "non-alphanumeric characters with a single hyphen, and strips leading/"
            "trailing hyphens. Reply with a single ```python code block."}],
        "tests": "assert slugify('Hello,  World!') == 'hello-world'\n"
                 "assert slugify('  a  ') == 'a'\n"
                 "assert slugify('A--B') == 'a-b'\n",
    },
]

CODE_RE = re.compile(r"```(?:python)?\s*(.*?)```", re.DOTALL)


def _completion_text(completion):
    if isinstance(completion, str):
        return completion
    if isinstance(completion, list) and completion and isinstance(completion[0], dict):
        return completion[0].get("content", "")
    return ""


def code_reward(completions, tests, **kwargs):
    rewards = []
    for completion, test_src in zip(completions, tests):
        text = _completion_text(completion)
        m = CODE_RE.search(text)
        code = m.group(1) if m else text
        test_lines = [ln for ln in test_src.splitlines() if ln.strip()]
        passed = 0
        with tempfile.TemporaryDirectory() as td:
            for i, line in enumerate(test_lines):
                path = os.path.join(td, f"t{i}.py")
                with open(path, "w") as f:
                    f.write(code + "\n" + line + "\n")
                try:
                    r = subprocess.run([sys.executable, path], capture_output=True, timeout=5)
                    passed += (r.returncode == 0)
                except subprocess.TimeoutExpired:
                    pass
        rewards.append(passed / len(test_lines))
    return rewards


dataset = Dataset.from_list(TASKS * 20)  # 40 rows, plenty for 10 steps

# TRL renames GRPOConfig fields across versions; keep only what this one accepts.
wanted = dict(
    output_dir="grpo_smoke_out",
    per_device_train_batch_size=4,
    num_generations=4,
    max_prompt_length=512,
    max_prompt_len=512,
    max_completion_length=300,
    max_completion_len=300,
    max_new_tokens=300,
    max_steps=10,
    learning_rate=1e-5,
    logging_steps=1,
    fp16=True,          # T4 has no bf16
    report_to="none",
    temperature=0.8,
    save_strategy="no",
)
valid = {f.name for f in dataclasses.fields(GRPOConfig)}
dropped = sorted(k for k in wanted if k not in valid)
print(f"[setup] GRPOConfig args dropped as unsupported: {dropped}")
args = GRPOConfig(**{k: v for k, v in wanted.items() if k in valid})

peft_config = LoraConfig(
    r=16, lora_alpha=32, lora_dropout=0.0, task_type="CAUSAL_LM",
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
)

t1 = time.time()
trainer = GRPOTrainer(
    model=MODEL,
    reward_funcs=code_reward,
    args=args,
    train_dataset=dataset,
    peft_config=peft_config,
)
print(f"[setup] trainer built in {time.time() - t1:.0f}s")

t2 = time.time()
trainer.train()
train_secs = time.time() - t2

rewards = [h.get("reward") for h in trainer.state.log_history if "reward" in h]
print(f"[result] 10 GRPO steps in {train_secs:.0f}s ({train_secs / 10:.1f}s/step)")
print(f"[result] per-step mean reward: {[round(r, 3) for r in rewards]}")
if torch.cuda.is_available():
    print(f"[result] peak GPU mem: {torch.cuda.max_memory_allocated() / 1e9:.2f} GB")
print(f"[result] total wall time: {time.time() - t0:.0f}s")
print("SMOKE OK")
