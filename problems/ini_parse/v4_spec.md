Update from the client: "files sometimes repeat a section header — sections
with the same name should just work sensibly." We asked what "sensibly"
means and pinned it down: duplicate `[name]` headers all refer to ONE
section — merge their keys into a single dict — and the first-value-wins
rule for duplicate keys applies across the merged section as a whole, in
file order. (An explicit `[]` header names the same `""` section that
pre-header key lines go into.)
