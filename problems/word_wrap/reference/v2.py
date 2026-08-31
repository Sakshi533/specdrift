def wrap(text, width):
    words = []
    for w in text.split():
        if len(w) > width:
            words.extend(w[i:i + width] for i in range(0, len(w), width))
        else:
            words.append(w)
    lines = []
    cur = []
    cur_len = 0
    for w in words:
        if not cur:
            cur, cur_len = [w], len(w)
        elif cur_len + 1 + len(w) <= width:
            cur.append(w)
            cur_len += 1 + len(w)
        else:
            lines.append(" ".join(cur))
            cur, cur_len = [w], len(w)
    if cur:
        lines.append(" ".join(cur))
    return lines
