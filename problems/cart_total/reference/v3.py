def cart_total(items):
    lines = [it["unit_price"] * it["qty"] for it in items]
    qualifying = [i for i, it in enumerate(items) if it["qty"] >= 10]
    if qualifying:
        best = max(qualifying, key=lambda i: (lines[i], -i))
        lines[best] = lines[best] * 9 // 10
    return sum(lines)
