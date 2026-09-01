# SpecDrift

An executable benchmark — and RL environment — for how language models handle
**changing requirements mid-task**.

Static benchmarks (HumanEval, MBPP, SWE-bench) hand a model one frozen spec.
Real engineering doesn't work that way: constraints get added, contradicted,
and walked back mid-implementation. SpecDrift measures whether a model can
apply a requirement update **without silently breaking constraints that still
hold** — and then uses the same environment as a verifiable-reward signal to
RL-train a small open model (GRPO) to get better at it.

## How it works

Each problem is a base spec plus a sequence of update messages, delivered one
per turn like a client changing their mind. Every version `k` has a hidden
test suite valid *at that version*, with each test **origin-tagged** by the
version that introduced (or last rewrote) its constraint:

- `test_v3_*` failing at version 3 → the model missed the **new** requirement
- `test_v1_*` failing at version 3 → the model **regressed** a constraint that
  still holds (this is the interesting metric)

Contradicted constraints are rewritten with a new origin tag, so carried tests
are valid by construction. Per turn we report `current_pass_rate` and
`regression_rate`; the scalar `reward` (0.6·current + 0.4·(1−regression)) is
the RL training signal.

Every problem is machine-validated (`python -m specdrift.validate`) against
three authoring rules:

- **R1** — the version-`k` reference solution passes version `k`'s full suite
- **R2** — the version-`k−1` reference *fails* at least one new-origin test
  (every update is provably non-trivial)
- **R3** — the version-`k−1` reference passes all carried tests (no stale
  tests for contradicted constraints)

## Layout

```
specdrift/          harness: sandboxed test runner, scoring, rollout protocol, validator
problems/<id>/      problem.json, v{k}_spec.md, v{k}_tests.py, reference/v{k}.py
kaggle_smoke/       GRPO feasibility kernel (Qwen2.5-Coder-0.5B + LoRA on a T4)
```

## Status

- [x] Harness + validator + multi-turn rollout protocol
- [x] 3 pilot problem families × 4 versions (all rules green)
- [x] GRPO-on-T4 smoke test: 10 steps in 150s (15s/step), peak 4.7 GB VRAM,
      Qwen2.5-Coder-0.5B + LoRA, TRL 1.12, executable-test rewards flowing
- [x] 12 problem families × 4 versions across the update-type taxonomy
- [x] Training pipeline pilot on T4 (20 steps, 15 min end-to-end): baseline
      eval → GRPO on 9 train problems → post-eval on 3 held-out problems.
      Baseline Qwen2.5-Coder-1.5B on held-out: 67% current-spec pass,
      **68% regression rate** — large headroom for training
- [x] 21 problem families (~600 tests) across all five update types,
      including `ambiguous`
- [x] First full GRPO run — see results below
- [ ] Frontier model evals (free tiers: Gemini, Groq)
- [ ] Longer training + larger eval split (current result is one seed on a
      5-problem holdout — directional, not definitive)

## Training results (GRPO, Qwen2.5-Coder-1.5B + LoRA, one free Kaggle T4)

Reward = executable tests only: 0.6·current-spec pass + 0.4·(1−regression).
Eval is multi-turn on held-out problems (the model sees its own prior
replies), three decoding passes (greedy + 2 sampled seeds @ T=0.7). Raw
records in `docs/results/`.

**Run 2 — 400 steps, 3.5 h, 25 train / 8 holdout problems:**

| holdout metric (96 episode-turns) | before | after | Δ |
|---|---|---|---|
| current-spec pass rate | 30.5% | 43.6% | **+13.1** |
| regression rate (old constraints broken) | 78.1% | 60.0% | **−18.1** |

Per decoding pass — before → after (current / regression):
greedy 44.6→47.5 / 60.7→51.4 · seed-0 25.2→52.5 / 88.6→42.9 ·
seed-1 21.6→30.9 / 85.0→85.7. The biggest gains are under sampling — the
base model falls apart at T=0.7 and training largely fixes that — but the
seed-1 regression staying flat shows the spread is real; treat the aggregate
as the estimate and the passes as its error bar.

By update type (current pass / regression, after training): robustness
79.5/53.3 · contradicting 25.8/56.9 · additive 23.0/53.1 · ambiguous
20.8/84.2 — ambiguous updates barely improved and remain the failure mode;
interface updates show 0% regression by construction (a return-shape change
re-pins all constraints as current). Turn-1 (fresh spec, no churn) also rose
56.8→76.6, so part of the gain is general task competence, not only
churn-handling — separating those is future work.

Run 1 (150 steps, 5-problem holdout, greedy only) showed the same direction
smaller: regression 68.0→59.8, current-pass flat. Training reward in both
runs was still climbing at cutoff.
