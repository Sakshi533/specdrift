Update: bad strings are reaching the comparator and silently producing
garbage orderings. Validate BOTH arguments before comparing and raise
`ValueError` for any invalid one: the empty string, any numeric component
that is empty or contains anything but ASCII digits `0-9` (so `"1..2"`,
`"1.x"`, `"1. 2"`, `"+1.0"` are all invalid), and a `-` with nothing after
it (empty pre-release tag, `"1.0-"`). Any non-empty tag remains acceptable.
Valid inputs compare exactly as they do today.
