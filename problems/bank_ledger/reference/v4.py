def apply_txns(balance, txns):
    fees = 0
    for t in txns:
        balance += t
        if balance < 0:
            balance -= 50
            fees += 50
    return balance, fees
