def assign(rows, parties):
    free = list(rows)
    out = []
    for p in parties:
        idx = -1
        for i, f in enumerate(free):
            if f >= p:
                idx = i
                break
        if idx >= 0:
            free[idx] -= p
        out.append(idx)
    return out
