Write a Python function `assign(rows, parties)`.

`rows` is a list of ints: the number of free seats in each row. `parties` is
a list of ints: party sizes, processed in order. Each party is seated
entirely in the FIRST row (lowest index) that still has enough free seats --
a party is never split across rows. Seating a party reduces that row's free
seats. A party that fits in no row is skipped (the rows are left untouched).
Return a list of row indices, one per party in order, with `-1` for a
skipped party.
