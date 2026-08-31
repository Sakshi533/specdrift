def fold(lines):
    out = []
    for line in lines:
        if line and line[0] in " \t":
            body = line.lstrip()
            if out:
                out[-1] = out[-1] + " " + body
            else:
                out.append(body)
        else:
            out.append(line)
    return out
