def apply_txns(balance, txns):
    for t in txns:
        balance += t
        if balance < 0:
            balance -= 50
    return balance
