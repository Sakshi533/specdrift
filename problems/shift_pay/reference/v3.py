DAY = 1440
NIGHT_START = 1320


def _night_minutes(shifts):
    night = 0
    for start, end in shifts:
        for day in range(start // DAY, (end - 1) // DAY + 1):
            lo = max(start, day * DAY + NIGHT_START)
            hi = min(end, (day + 1) * DAY)
            if hi > lo:
                night += hi - lo
    return night


def _night_overtime_minutes(shifts):
    """Night minutes among the worked minutes after the first 2400 (chronological)."""
    overlap = 0
    worked = 0
    for start, end in shifts:
        length = end - start
        if worked + length > 2400:
            ot_start = start + max(0, 2400 - worked)
            overlap += _night_minutes([(ot_start, end)])
        worked += length
    return overlap


def pay(shifts, rate):
    total = sum(end - start for start, end in shifts)
    overtime = max(0, total - 2400)
    night = _night_minutes(shifts)
    night_regular = night - _night_overtime_minutes(shifts)
    base = total * rate
    night_bonus = night_regular * rate // 4
    overtime_bonus = overtime * rate // 2
    return base + night_bonus + overtime_bonus
