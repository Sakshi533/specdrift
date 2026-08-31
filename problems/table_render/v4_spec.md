Update: callers keep writing `"\n".join(render(rows))` themselves, so fold
it in. `render` now returns a SINGLE STRING — the same lines as today,
joined with `"\n"` (no trailing newline). `render([])` returns `""`. No
other behavior changes.
