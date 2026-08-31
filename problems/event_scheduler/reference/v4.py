def can_book(bookings, start, end):
    if start < 0 or end <= start:
        return False
    return all(end <= s or e <= start for s, e in bookings)
