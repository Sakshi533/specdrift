import re

_TERM = re.compile(r"([0-9]+)([dhms])")
_MULT = {"d": 86400, "h": 3600, "m": 60, "s": 1}


def secs(s):
    total = 0
    for value, unit in _TERM.findall(s):
        total += int(value) * _MULT[unit]
    return total
