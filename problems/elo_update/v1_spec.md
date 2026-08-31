Write a Python function `update(ra, rb, result)`.

`ra` and `rb` are int Elo ratings for players A and B; `result` is `"a"` (A
won), `"b"` (B won) or `"draw"`. With K = 32, A's expected score is
`Ea = 1 / (1 + 10 ** ((rb - ra) / 400))` and A's actual score `Sa` is 1, 0 or
0.5 respectively. A's rating change is

    delta_a = round_half_up(32 * (Sa - Ea))

where `round_half_up(x) = math.floor(x + 0.5)` — exact halves round toward
+infinity (2.5 -> 3, -2.5 -> -2). Floats are fine internally; this rounding
definition is exact and pinned. The update is zero-sum: return the new int
ratings as the tuple `(ra + delta_a, rb - delta_a)`.
