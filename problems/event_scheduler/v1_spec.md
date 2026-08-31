Write a Python function `can_book(bookings, start, end)`.

`bookings` is a list of `(start, end)` tuples of ints (minutes since the start
of the day), each a half-open interval `[start, end)`. The requested slot is
`[start, end)` in the same units. Return `True` if the slot can be booked —
i.e. it overlaps no existing booking — and `False` otherwise. Two half-open
intervals overlap when each one starts before the other ends. An empty
calendar has no conflicts.
