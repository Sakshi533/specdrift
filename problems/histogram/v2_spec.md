Update from the stats team: silently dropping out-of-range values keeps hiding
data problems. `bins` must now return a tuple `(under, counts, over)`:
`under` is the number of values below `edges[0]`, `over` is the number of
values at or above `edges[-1]`, and `counts` is the same per-bin list as
before.
