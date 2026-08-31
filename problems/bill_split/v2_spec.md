Update: some diners want to pay proportionally. `split(total, weights)` must
now also accept a list of positive int weights, one per person; person i's
share is proportional to `weights[i]`. Everything stays whole cents and must
still sum to exactly `total`: give everyone the floor of their exact
proportional share (`total * w // sum(weights)`), then hand out the remaining
cents one each in order of LARGEST fractional remainder first (on a tie,
lowest index first). Passing an int `n` must keep working exactly as before —
treat it as `n` equal weights.
