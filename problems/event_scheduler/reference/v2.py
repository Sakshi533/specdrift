def can_book(bookings, start, end):
    return all(end + 15 <= s or e + 15 <= start for s, e in bookings)
