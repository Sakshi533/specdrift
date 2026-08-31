def trace(capacity, ops):
    order = []      # keys, least-recently-used first
    data = {}
    out = []
    for op in ops:
        if op[0] == "put":
            _, k, v = op
            data[k] = v
            if k in order:
                order.remove(k)
            order.append(k)
            if len(order) > capacity:
                del data[order.pop(0)]
        else:
            _, k = op
            if k in data:
                order.remove(k)
                order.append(k)
                out.append(data[k])
            else:
                out.append(None)
    return out
