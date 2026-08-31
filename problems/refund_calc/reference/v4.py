def refund(price, days, opened):
    if price < 0 or days < 0:
        raise ValueError("price and days must be non-negative")
    if days <= 14:
        r = price
    elif days <= 30:
        r = price // 2
    else:
        r = 0
    if opened:
        r = max(0, r - 500) // 2
    return r
