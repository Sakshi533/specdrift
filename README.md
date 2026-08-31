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
- [ ] Scale to ~30-40 problems (add `ambiguous` type; raise difficulty —
      bank_ledger is already saturated by a 1.5B model)
- [ ] Frontier model evals (free tiers: Gemini, Groq)
- [ ] Full GRPO run (~300 steps ≈ 2h) + before/after comparison
