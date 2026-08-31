def allow(events, limit, window):
    allowed = {}
    out = []
    for ev in events:
        t, key = ev if isinstance(ev, tuple) else (ev, None)
        bucket = allowed.setdefault(key, [])
        n = sum(1 for a in bucket if t - window < a <= t)
        ok = n + 1 <= limit
        out.append(ok)
        if ok:
            bucket.append(t)
    return out
