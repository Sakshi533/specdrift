def allow(events, limit, window):
    seen = {}
    out = []
    for ev in events:
        t, key = ev if isinstance(ev, tuple) else (ev, None)
        bucket = seen.setdefault(key, [])
        n = sum(1 for a in bucket if t - window < a <= t)
        out.append(n + 1 <= limit)
        bucket.append(t)
    return out
