Write a Python function `split_row(line)` that splits a single CSV line into
a list of field strings.

Rules: split on every comma. No quote handling — a double-quote character is
just an ordinary character. No trimming — whitespace is part of the field and
must be kept as-is. Empty fields are allowed: `"a,,c"` gives three fields
`["a", "", "c"]`.
