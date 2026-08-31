def fold(lines):
    folded = []
    for line in lines:
        if line and line[0] in " \t":
            body = line.lstrip()
            if folded:
                folded[-1] = folded[-1] + " " + body
            else:
                folded.append(body)
        else:
            folded.append(line)

    runs = []
    for line in folded:
        if runs and runs[-1][0] == line:
            runs[-1][1] += 1
        else:
            runs.append([line, 1])
    return [text + " (x%d)" % n if n >= 2 else text for text, n in runs]
