Write a Python function `fold(lines)` where `lines` is a list of log-line
strings (no trailing newlines). Return the folded list of lines.

A line that starts with a space or tab is a CONTINUATION of the previous
line: fold it into the previous output line by replacing its leading run of
whitespace with a single space and appending the rest. Continuations chain —
several continuation lines in a row all fold into the same output line, in
order. Whitespace inside the line (after the leading run) is preserved
exactly.

A continuation with no previous line (i.e. at the very start of the input)
stands alone as its own output line, with its leading whitespace stripped.
Every other line starts a new output line, unchanged.
