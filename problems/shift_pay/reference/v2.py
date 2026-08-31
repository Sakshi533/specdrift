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


def pay(shifts, rate):
    total = sum(end - start for start, end in shifts)
    overtime = max(0, total - 2400)
    base = total * rate
    night_bonus = _night_minutes(shifts) * rate // 4
    overtime_bonus = overtime * rate // 2
    return base + night_bonus + overtime_bonus
