def cart_total(items):
    return sum(it["unit_price"] * it["qty"] for it in items)
