def assign(rows, parties):
    free = list(rows)
    out = []
    for p in parties:
        idx = -1
        for i, f in enumerate(free):
            if f >= p and (idx == -1 or f < free[idx]):
                idx = i
        if idx >= 0:
            free[idx] -= p
        out.append(idx)
    return out
