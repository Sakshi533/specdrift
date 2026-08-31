Update: hardening against garbage from the floor app. A party size of zero
or less must raise `ValueError`. An empty `rows` list is legal: every party
is simply skipped with -1. An empty `parties` list returns `[]`. No other
validation.
