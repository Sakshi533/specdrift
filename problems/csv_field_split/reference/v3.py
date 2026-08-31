def split_row(line):
    fields = []
    buf = []
    in_quotes = False
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == '"':
            if in_quotes and i + 1 < len(line) and line[i + 1] == '"':
                buf.append('"')
                i += 1
            else:
                in_quotes = not in_quotes
        elif ch == "," and not in_quotes:
            fields.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
        i += 1
    fields.append("".join(buf))
    return fields
