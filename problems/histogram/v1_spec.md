Write a Python function `bins(values, edges)`.

`values` is a list of ints; `edges` is a sorted list of ints with
`len(edges) >= 2`. Bin `i` is the half-open interval `[edges[i], edges[i+1])`.
Return a list of `len(edges) - 1` ints: how many values fall in each bin.
Values that fall in no bin are ignored. The result must be deterministic.
