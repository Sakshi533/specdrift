def apply_txns(balance, txns):
    for t in txns:
        if balance + t >= 0:
            balance += t
    return balance
