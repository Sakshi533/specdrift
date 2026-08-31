Update: garbage inputs must fail loudly now. Raise `ValueError` when the
input is empty or whitespace-only, or when any whitespace-separated token is
not exactly digits-then-unit-letter — that covers unknown units (`"5x"`),
bare numbers (`"12"`), bare units (`"h"`), and negative values (`"-5m"`).
To be explicit about the floor: `"0s"` is a valid duration and returns `0`.
Repeats and arbitrary order stay legal.
