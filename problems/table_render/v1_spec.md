Write a Python function `render(rows)` that renders a table as text.
`rows` is a list of rows; each row is a list of cell strings. Return a LIST
of output lines, one per input row, in order.

Rules:

- The table has as many columns as the WIDEST row. Shorter (ragged) rows are
  first padded with empty-string cells on the right up to that width; the
  padding cells take part in everything below like any other cell.
- Each column's width is the length of the longest cell in that column
  (after ragged padding).
- Every cell is left-aligned: padded on the right with spaces to its
  column's width.
- The padded cells of a row are joined with `" | "` (space, pipe, space),
  and then any TRAILING whitespace is stripped from the joined line. (Only
  trailing — inner padding and separators stay exactly as built, so a line
  can legitimately end in `|` when its last cells are empty.)
- `render([])` returns `[]`.
