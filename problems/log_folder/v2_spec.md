Update: the dashboard drowns in repeats. After folding, collapse each run of
consecutive IDENTICAL output lines into a single line with the suffix
` (xN)`, where N is the run length. Only for N >= 2 — a line that appears
once stays exactly as-is. Example: two identical folded lines `disk full`
become the single line `disk full (x2)`. Non-adjacent repeats are NOT
collapsed.
