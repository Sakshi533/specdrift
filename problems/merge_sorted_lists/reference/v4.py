def merge(a, b):
    a = a or []
    b = b or []
    ta = [(x, 'a') for x in a]
    tb = [(x, 'b') for x in b]
    out = []
    i = j = 0
    while i < len(ta) and j < len(tb):
        if ta[i][0] <= tb[j][0]:
            out.append(ta[i]); i += 1
        else:
            out.append(tb[j]); j += 1
    out.extend(ta[i:])
    out.extend(tb[j:])
    return out
