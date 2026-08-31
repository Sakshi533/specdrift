def trace(capacity, ops):
    order = []      # keys, least-recently-used first
    data = {}
    results = []
    evicted = []
    hits = 0
    misses = 0
    for op in ops:
        kind = op[0]
        if kind == "put":
            _, k, v = op
            if k in data:
                data[k] = v          # value update keeps its old position
            else:
                data[k] = v
                order.append(k)
                if len(order) > capacity:
                    gone = order.pop(0)
                    del data[gone]
                    evicted.append(gone)
        else:  # get or peek
            _, k = op
            if k in data:
                hits += 1
                if kind == "get":
                    order.remove(k)
                    order.append(k)
                results.append(data[k])
            else:
                misses += 1
                results.append(None)
    return {"results": results, "evicted": evicted, "hits": hits, "misses": misses}
