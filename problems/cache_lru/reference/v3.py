def trace(capacity, ops):
    order = []      # keys, least-recently-used first
    data = {}
    out = []
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
                    del data[order.pop(0)]
        elif kind == "get":
            _, k = op
            if k in data:
                order.remove(k)
                order.append(k)
                out.append(data[k])
            else:
                out.append(None)
        else:  # peek: read without touching recency
            out.append(data.get(op[1]))
    return out
