def price(base, rules):
    p = base
    steps = []
    for kind, val in rules:
        if kind == "percent":
            p = max(0, p - base * val // 100)
        elif kind == "flat":
            p = max(0, p - val)
        else:  # cap: total discount so far may not exceed val
            p = max(p, base - val)
        steps.append(p)
    return {"final": p, "total_discount": base - p, "steps": steps}
