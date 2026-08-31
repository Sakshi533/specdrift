import re

_TERM = re.compile(r"([0-9]+)([dhms])\Z")
_MULT = {"d": 86400, "h": 3600, "m": 60, "s": 1}


def secs(s):
    tokens = s.split()
    if not tokens:
        raise ValueError("empty duration")
    total = 0
    for token in tokens:
        m = _TERM.match(token)
        if m is None:
            raise ValueError(f"bad term: {token!r}")
        total += int(m.group(1)) * _MULT[m.group(2)]
    return total
