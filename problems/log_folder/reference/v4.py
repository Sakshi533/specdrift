def fold(lines):
    folded = []
    open_group = False
    for line in lines:
        if line is None:
            raise ValueError("None entry in log lines")
        if line == "":
            open_group = False
            continue
        if line[0] in " \t":
            body = line.lstrip()
            if open_group:
                folded[-1] = folded[-1] + " " + body
            else:
                folded.append(body)
                open_group = True
        else:
            folded.append(line)
            open_group = True

    runs = []
    for line in folded:
        if runs and runs[-1][0] == line:
            runs[-1][1] += 1
        else:
            runs.append([line, 1])
    return ["%d x %s" % (n, text) if n >= 2 else text for text, n in runs]
