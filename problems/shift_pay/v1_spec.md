Write a Python function `pay(shifts, rate)`.

`shifts` is a list of `(start_min, end_min)` int tuples — minutes since the
start of the week (`0 <= start < end <= 10080`), non-overlapping and sorted by
start. `rate` is the pay rate in cents per minute (int, >= 1). Worked minutes
beyond 2400 in the week are overtime, paid at 1.5x. Keep everything in exact
integer arithmetic and floor once, at the end, in the overtime term:

    total    = sum of shift lengths in minutes
    overtime = max(0, total - 2400)
    pay      = (total - overtime) * rate + overtime * rate * 3 // 2

Return the pay in cents as an int.
