Update: our exports now quote some fields. A field may be wrapped in double
quotes, and a quoted field can contain commas — do NOT split on a comma that
is inside quotes. The surrounding quotes themselves are stripped from the
output. Everything else stays as it was.
Example: `a,"b,c",d` -> `["a", "b,c", "d"]`.
