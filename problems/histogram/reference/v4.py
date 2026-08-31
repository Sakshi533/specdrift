import bisect


def bins(values, edges):
    counts = [0] * (len(edges) - 1)
    under = over = 0
    catch = {}  # edge value -> index of FIRST zero-width bin with that edge
    for i in range(len(edges) - 1):
        if edges[i] == edges[i + 1] and edges[i] not in catch:
            catch[edges[i]] = i
    for v in values:
        if v <= edges[0]:
            under += 1
        elif v > edges[-1]:
            over += 1
        elif v in catch:
            counts[catch[v]] += 1
        else:
            counts[bisect.bisect_left(edges, v) - 1] += 1
    return under, counts, over
