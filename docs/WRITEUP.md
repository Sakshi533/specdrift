# SpecDrift: teaching a small model to survive changing requirements (draft)

*Status: working draft — numbers final for runs 1–2, prose to be polished.*

## The problem nobody benchmarks

Every popular code benchmark hands the model a frozen spec. Real engineering
churns: constraints get added mid-task, contradicted, walked back. The
interesting failure isn't "can't solve the problem" — it's **silently breaking
something that already worked** while applying an update. That failure is
invisible to single-spec benchmarks by design.

Related work gets close but not there: Laban et al. (2025, "LLMs Get Lost in
Multi-Turn Conversation") shard specs across turns and show degradation, but
score only final-task success; editing benchmarks (CodeEditorBench, Aider)
target a static goal; instruction-following suites (FollowBench, Multi-IF)
don't execute code. SpecDrift's contribution is the combination: **sequential
spec churn + executable per-version test suites + explicit regression
accounting**, plus using the same environment as a verifiable RL reward.

## Design in one paragraph

33 problem families × 4 spec versions. Each version's hidden suite is
origin-tagged: `test_v1_*` failing at turn 3 means a regression on a
still-valid old constraint; `test_v3_*` failing means the new requirement was
missed. Contradicted constraints are rewritten with a new origin, so carried
tests are valid by construction. Three machine-checked authoring rules keep
the benchmark honest: the reference passes everything (R1), every update
provably breaks the previous version's reference (R2 — no filler updates),
and no stale tests survive a contradiction (R3). Updates are labeled
additive / contradicting / interface / robustness / ambiguous.

## What a 1.5B coder model does under churn

Qwen2.5-Coder-1.5B-Instruct, multi-turn, on 8 held-out problems (3 decoding
passes): 30.5% current-spec pass, **78.1% regression rate**. Turn 1 (fresh
spec) is fine (57% greedy); the moment updates start, both compliance and
stability collapse. Contradicting and ambiguous updates are the worst
categories — the model tends to either ignore the walk-back or rewrite code
wholesale and lose earlier constraints.

## GRPO with executable rewards, on a free Kaggle T4

Reward = 0.6·(current-spec pass rate) + 0.4·(1 − regression rate), computed
by actually running the hidden tests on each rollout. LoRA r=16, 8 rollouts
per step, teacher-forced context (reference code stands in for prior turns).
400 steps ≈ 3.5 h on a single free T4 — the entire training story fits in
free-tier compute.

Result on the held-out problems (96 episode-turns per side):

- current-spec pass **30.5% → 43.6%**
- regression rate **78.1% → 60.0%**

Gains are largest under sampling (the base model degrades badly at T=0.7;
seed-0 regression 88.6→42.9), visible but smaller under greedy decoding
(60.7→51.4). Seed variance is real — one sampled seed's regression didn't
move — so we report the aggregate with the per-pass spread rather than a
single flattering number.

By update type after training: robustness is largely solved (79.5% current),
contradicting and additive improved materially on regression (~−26 pts),
**ambiguous updates barely moved (20.8% current, 84.2% regression)** —
under-specified requirements remain the open failure mode RL didn't fix.
Turn-1 performance also rose (56.8→76.6), meaning part of the gain is general
competence rather than churn-handling specifically; disentangling the two
(e.g. a turn-1-only training control) is the clearest next experiment.

## Where frontier models stand

Running frontier-tier models through the full benchmark (greedy, free API
tiers) reframes the picture: gemini-3.5-flash-lite scores 95.1% current-spec
pass with 3.3% regression, qwen3.8-27B 95.1%/5.7%, gpt-oss-120B 88.7%/15.9%.
Function-level spec churn is largely a solved problem at that scale — **with
one systematic exception: interface-change updates, where the two top models
break 42.9% of carried constraints and gpt-oss-120B breaks 71.4%**. When a
return shape changes, even frontier-tier models lose behavioral constraints
they were supposed to preserve. gpt-oss-120B also shows genuine multi-turn
degradation (96.6% → 83.8% current-pass across turns).

This is the honest headline for the benchmark: its dynamic range lives in
the gap between small open models (78% regression) and frontier ones (~3–6%),
which makes it (a) a calibrated measure of how far small models are from
frontier churn-robustness, (b) evidence that verifiable-reward RL closes part
of that gap on free compute, and (c) saturated at the frontier for
function-level tasks — repository-scale problems and longer update chains are
the v2 direction for challenging top models.

## Honest limitations

One base model, one training seed, 8 holdout families, 3 decoding passes.
The sandbox is a subprocess with a timeout, not a hardened jail. Problems are
function-level Python, not repository-scale — sufficient to expose the
small-model failure mode, insufficient to challenge frontier models except on
interface churn. None of this blocks the core claims: the failure mode is
real, measurable, and partially trainable away with verifiable rewards on
free compute.

## Reproduce

Everything (harness, 33 problems, training kernel, raw eval records) is in
the repo. `python -m specdrift.validate` checks the benchmark's own rules;
`kaggle_train/grpo_train.py` is the exact training script; `specdrift/
analysis.py` regenerates every table here from `docs/results/*.jsonl`.
