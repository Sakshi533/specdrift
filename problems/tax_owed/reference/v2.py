def tax(income):
    taxable = max(income - 50000, 0)
    at_10 = min(max(taxable - 100000, 0), 400000)
    at_20 = max(taxable - 500000, 0)
    return at_10 // 10 + at_20 // 5
