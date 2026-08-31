Write a Python function `secs(s)` that parses a duration string like
`"2h 30m 15s"` and returns the total number of seconds as an `int`.

The input format:

- The string is a sequence of one or more TERMS separated by single spaces;
  the whole string consists of terms — nothing before, between, or after
  them except those single separator spaces.
- A term is a value directly followed by a unit letter: `h` (hours, 3600 s),
  `m` (minutes, 60 s), or `s` (seconds). The value is one or two ASCII
  digits (0-99), e.g. `"5s"`, `"45m"`.
- Each unit appears AT MOST ONCE, and the terms that are present appear in
  `h`, `m`, `s` order (any subset is fine: `"1h 5s"`, `"45m"`).

You only need to handle strings of this shape.
