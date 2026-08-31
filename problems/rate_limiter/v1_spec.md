Write a Python function `allow(events, limit, window)`.

`events` is a list of int timestamps in seconds, sorted ascending. Return a
list of bools, one per event, in order. An event at time `t` is allowed iff
the number of ALLOWED events whose timestamp falls in the half-open window
`(t - window, t]` -- counting the event itself -- would be at most `limit`.
Denied events do NOT consume quota: they never count toward the window for
any later event. `limit >= 1` and `window >= 1` always hold.
