Update from the rating committee: players rated under 1000 are provisional
and should move faster. Zero-sum is dropped — each side now computes its own
delta with its own K, where a player's K is 64 if their current (pre-update)
rating is below 1000, else 32:

    delta_a = round_half_up(Ka * (Sa - Ea))
    delta_b = round_half_up(Kb * (Sb - Eb))

with `Sb = 1 - Sa`, `Eb = 1 / (1 + 10 ** ((ra - rb) / 400))`, and the same
pinned round_half_up. Return `(ra + delta_a, rb + delta_b)`.
