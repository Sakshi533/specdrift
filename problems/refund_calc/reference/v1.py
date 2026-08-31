def refund(price, days, opened):
    if days <= 14:
        r = price
    elif days <= 30:
        r = price // 2
    else:
        r = 0
    if opened:
        r = r // 2
    return r
