def tax(income):
    taxable = max(income - 50000, 0) if income <= 800000 else income
    at_10 = min(max(taxable - 100000, 0), 400000)
    at_20 = max(taxable - 500000, 0)
    amount = at_10 // 10 + at_20 // 5
    rate = round(amount / income, 4) if income > 0 else 0.0
    return {"tax": amount, "effective_rate": rate}
