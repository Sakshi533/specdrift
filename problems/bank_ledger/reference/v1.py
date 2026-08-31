def apply_txns(balance, txns):
    for t in txns:
        balance += t
    return balance
