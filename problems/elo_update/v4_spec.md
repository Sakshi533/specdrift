Update: the UI team needs the deltas, not just the new ratings. `update` must
now return a dict `{"a": int, "b": int, "delta_a": int, "delta_b": int}` —
the new ratings plus each side's applied change, so `a == ra + delta_a` and
`b == rb + delta_b` (for zero-sum mixed pairs `delta_b == -delta_a`). No
rating math changes.
