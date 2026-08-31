def allow(events, limit, window):
    seen = {}       # key -> timestamps that consume quota
    first = {}      # (key, t) -> was the first event here allowed?
    out = []
    for ev in events:
        t, key = ev if isinstance(ev, tuple) else (ev, None)
        if first.get((key, t)):
            out.append(True)        # piggyback: free ride, consumes nothing
            continue
        bucket = seen.setdefault(key, [])
        n = sum(1 for a in bucket if t - window < a <= t)
        ok = n + 1 <= limit
        if (key, t) not in first:
            first[(key, t)] = ok
        out.append(ok)
        bucket.append(t)
    return out
