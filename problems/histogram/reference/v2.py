import bisect


def bins(values, edges):
    counts = [0] * (len(edges) - 1)
    under = over = 0
    for v in values:
        if v < edges[0]:
            under += 1
        elif v >= edges[-1]:
            over += 1
        else:
            counts[bisect.bisect_right(edges, v) - 1] += 1
    return under, counts, over
