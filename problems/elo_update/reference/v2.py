import math

_SCORE = {"a": 1.0, "b": 0.0, "draw": 0.5}


def _round_half_up(x):
    return math.floor(x + 0.5)


def _k(rating):
    return 64 if rating < 1000 else 32


def update(ra, rb, result):
    sa = _SCORE[result]
    sb = 1.0 - sa
    ea = 1 / (1 + 10 ** ((rb - ra) / 400))
    eb = 1 / (1 + 10 ** ((ra - rb) / 400))
    delta_a = _round_half_up(_k(ra) * (sa - ea))
    delta_b = _round_half_up(_k(rb) * (sb - eb))
    return ra + delta_a, rb + delta_b
