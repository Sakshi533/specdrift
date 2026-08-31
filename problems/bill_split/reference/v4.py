def split(total, weights):
    if isinstance(weights, int):
        weights = [1] * weights
    if all(w == 0 for w in weights):
        raise ValueError("weights must not be all zero")
    w_sum = sum(weights)
    shares = [total * w // w_sum for w in weights]
    rems = [total * w % w_sum for w in weights]
    leftover = total - sum(shares)
    order = sorted((i for i, w in enumerate(weights) if w > 0),
                   key=lambda i: (rems[i], i))
    for i in order[:leftover]:
        shares[i] += 1
    return shares
