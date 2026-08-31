def cart_total(items):
    total = 0
    for it in items:
        line = it["unit_price"] * it["qty"]
        if it["qty"] >= 10:
            line = line * 9 // 10
        total += line
    return total
