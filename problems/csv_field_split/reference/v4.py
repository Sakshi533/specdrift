def split_row(line):
    fields = []
    buf = []
    in_quotes = False
    quoted = False
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == '"':
            if in_quotes and i + 1 < len(line) and line[i + 1] == '"':
                buf.append('"')
                i += 1
            else:
                in_quotes = not in_quotes
                quoted = True
        elif ch == "," and not in_quotes:
            field = "".join(buf)
            fields.append(field if quoted else field.strip())
            buf = []
            quoted = False
        else:
            buf.append(ch)
        i += 1
    field = "".join(buf)
    fields.append(field if quoted else field.strip())
    return fields
