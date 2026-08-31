def cmp(a, b):
    pa = [int(c) for c in a.split(".")]
    pb = [int(c) for c in b.split(".")]
    n = max(len(pa), len(pb))
    pa += [0] * (n - len(pa))
    pb += [0] * (n - len(pb))
    if pa < pb:
        return -1
    if pa > pb:
        return 1
    return 0
