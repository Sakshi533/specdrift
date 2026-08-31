import bisect


def bins(values, edges):
    counts = [0] * (len(edges) - 1)
    for v in values:
        if edges[0] <= v < edges[-1]:
            counts[bisect.bisect_right(edges, v) - 1] += 1
    return counts
