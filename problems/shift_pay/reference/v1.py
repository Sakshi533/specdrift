def pay(shifts, rate):
    total = sum(end - start for start, end in shifts)
    overtime = max(0, total - 2400)
    return (total - overtime) * rate + overtime * rate * 3 // 2
