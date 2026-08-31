def split_row(line):
    fields = []
    buf = []
    in_quotes = False
    for ch in line:
        if ch == '"':
            in_quotes = not in_quotes
        elif ch == "," and not in_quotes:
            fields.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    fields.append("".join(buf))
    return fields
