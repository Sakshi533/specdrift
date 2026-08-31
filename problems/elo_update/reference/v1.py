import math

_SCORE = {"a": 1.0, "b": 0.0, "draw": 0.5}


def _round_half_up(x):
    return math.floor(x + 0.5)


def update(ra, rb, result):
    ea = 1 / (1 + 10 ** ((rb - ra) / 400))
    delta_a = _round_half_up(32 * (_SCORE[result] - ea))
    return ra + delta_a, rb - delta_a
