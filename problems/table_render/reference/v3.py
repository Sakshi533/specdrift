def _is_int(cell):
    body = cell[1:] if cell.startswith("-") else cell
    return body != "" and all(ch in "0123456789" for ch in body)


def render(rows):
    if not rows:
        return []
    n_cols = max(len(row) for row in rows)
    padded = [list(row) + [""] * (n_cols - len(row)) for row in rows]
    widths = [max(len(row[c]) for row in padded) for c in range(n_cols)]
    lines = []
    for row in padded:
        cells = [row[c].rjust(widths[c]) if _is_int(row[c]) else row[c].ljust(widths[c])
                 for c in range(n_cols)]
        lines.append("  ".join(cells).rstrip())
    return lines
