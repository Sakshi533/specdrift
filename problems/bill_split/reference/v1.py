def split(total, n):
    base, rem = divmod(total, n)
    return [base + 1 if i < rem else base for i in range(n)]
