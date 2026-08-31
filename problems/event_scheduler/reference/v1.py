def can_book(bookings, start, end):
    return all(end <= s or e <= start for s, e in bookings)
