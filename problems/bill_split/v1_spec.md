Write a Python function `split(total, n)`.

`total` is a bill amount in cents (int, >= 0) and `n` is the number of people
(int, >= 1). Split the bill as evenly as possible using only whole cents:
return a list of `n` ints summing to exactly `total`. When the amount does
not divide evenly, the people EARLIER in the list get the extra cents — e.g.
`split(100, 3)` is `[34, 33, 33]`. The result must be deterministic.
