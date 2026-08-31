def tax(income):
    at_10 = min(max(income - 100000, 0), 400000)
    at_20 = max(income - 500000, 0)
    return at_10 // 10 + at_20 // 5
