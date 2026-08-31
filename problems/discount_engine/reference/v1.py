def price(base, rules):
    p = base
    for kind, val in rules:
        if kind == "percent":
            p -= p * val // 100
        else:  # flat
            p = max(0, p - val)
    return p
