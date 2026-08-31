# Authoring problems

## Update-type taxonomy

Every version-2+ update is labeled with exactly one primary type (goes in
`problem.json` later as `"update_types": {"2": "...", ...}`). The final
analysis slices scores by these — "which kind of churn breaks models?" is the
headline question of the writeup.

| type | meaning | example in pilots |
|---|---|---|
| `additive` | new constraint, everything else untouched | merge v2 (dedupe), slugify v2 (truncation), cart v2 (bulk discount) |
| `contradicting` | directly reverses an earlier constraint | merge v3 (un-dedupe + tags), slugify v3 (un-lowercase), cart v3 (discount walk-back) |
| `interface` | changes signature/return shape; behavior constraints persist | merge v3 (tuples), cart v4 (coupon kwarg) |
| `robustness` | edge-case hardening (empty/None/invalid input) | merge v4, slugify v4 |
| `ambiguous` | update is underspecified on purpose; tests pin the reasonable reading stated in a follow-up clarification sentence | none yet — add at scale-up |

A good problem mixes types across its versions and has at least one
`contradicting` update — those are where regression measurement earns its keep.

## Rules (machine-enforced by `python -m specdrift.validate`)

- **R1** — reference `v_k` passes all of `v{k}_tests.py`.
- **R2** — reference `v_{k-1}` fails ≥1 origin-`k` test (updates must be non-trivial).
- **R3** — reference `v_{k-1}` passes all carried (origin < k) tests. When an
  update contradicts an old constraint, delete or rewrite that test WITH THE
  NEW ORIGIN — a stale test would punish correct solutions.

## Style rules (not machine-enforced — review for these)

- Origin tag = version that introduced **or last rewrote** the constraint.
- Update specs are written as client messages (deltas), never restated full specs.
- Carried tests must use inputs that stay valid under later versions
  (e.g. slugify carried tests use lowercase inputs so the un-lowercase update
  doesn't invalidate them).
- Each version: 2–5 current-origin tests. Test one constraint per test where
  possible — regression attribution depends on it.
- Keep functions dependency-free, deterministic, CPU-instant. No I/O, no
  randomness, no wall-clock.
- Aim for updates whose naive implementation *interacts* with earlier code
  structure (the merge v3 type-change, the cart v3 "only one line" walk-back).
  An update a model can satisfy with one local edit measures nothing.
