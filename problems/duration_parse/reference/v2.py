import re

_TERM = re.compile(r"([0-9]+)([dhms])\Z")
_ORDER = "dhms"
_MULT = {"d": 86400, "h": 3600, "m": 60, "s": 1}


def secs(s):
    total = 0
    last = -1
    for token in s.split():
        m = _TERM.match(token)
        if m is None:
            raise ValueError(f"bad term: {token!r}")
        idx = _ORDER.index(m.group(2))
        if idx <= last:
            raise ValueError(f"unit out of order or repeated: {token!r}")
        last = idx
        total += int(m.group(1)) * _MULT[m.group(2)]
    return total
