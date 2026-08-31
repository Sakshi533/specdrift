def order(jobs):
    remaining = list(range(len(jobs)))
    out = []
    while remaining:
        top = max(jobs[i][1] for i in remaining)
        low = min(jobs[i][1] for i in remaining)
        pick = None
        if (len(out) + 1) % 4 == 0 and low < top:  # aging slot with >1 tier
            pick = min(i for i in remaining if jobs[i][1] == low)
        if pick is None:
            pick = min(remaining, key=lambda i: (-jobs[i][1], i))
        remaining.remove(pick)
        out.append(jobs[pick][0])
    return out
