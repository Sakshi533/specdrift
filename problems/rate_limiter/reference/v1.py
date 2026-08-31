def allow(events, limit, window):
    allowed = []
    out = []
    for t in events:
        n = sum(1 for a in allowed if t - window < a <= t)
        ok = n + 1 <= limit
        out.append(ok)
        if ok:
            allowed.append(t)
    return out
