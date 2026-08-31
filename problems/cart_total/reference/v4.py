def cart_total(items, coupon=0):
    if not 0 <= coupon <= 100:
        raise ValueError(f"coupon must be 0-100, got {coupon}")
    lines = [it["unit_price"] * it["qty"] for it in items]
    qualifying = [i for i, it in enumerate(items) if it["qty"] >= 10]
    if qualifying:
        best = max(qualifying, key=lambda i: (lines[i], -i))
        lines[best] = lines[best] * 9 // 10
    return sum(lines) * (100 - coupon) // 100
