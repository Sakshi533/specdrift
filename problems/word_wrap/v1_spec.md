Write a Python function `wrap(text, width)` that greedily word-wraps text.

Rules: split `text` on whitespace into words. Pack words left to right into
lines of at most `width` characters, joining the words on a line with single
spaces; when the next word would push the line past `width`, start a new
line. Return the list of lines. A single word longer than `width` gets a
line of its own and simply overflows.

Example: `wrap("the quick brown fox jumps", 10)` ->
`["the quick", "brown fox", "jumps"]`.
