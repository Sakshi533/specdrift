def split(total, weights):
    if isinstance(weights, int):
        weights = [1] * weights
    w_sum = sum(weights)
    shares = [total * w // w_sum for w in weights]
    rems = [total * w % w_sum for w in weights]
    leftover = total - sum(shares)
    order = sorted(range(len(weights)), key=lambda i: (rems[i], i))
    for i in order[:leftover]:
        shares[i] += 1
    return shares
