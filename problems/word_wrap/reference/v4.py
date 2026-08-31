ARTICLES = {"a", "an", "the"}


def wrap(text, width):
    if width < 1:
        raise ValueError("width must be at least 1")
    words = text.split()
    lines = []
    cur = []
    cur_len = 0
    i = 0
    while i < len(words):
        w = words[i]
        if not cur:
            cur, cur_len = [w], len(w)
            i += 1
        elif cur_len + 1 + len(w) <= width:
            cur.append(w)
            cur_len += 1 + len(w)
            i += 1
        else:
            while len(cur) > 1 and cur[-1] in ARTICLES:
                cur.pop()
                i -= 1
            lines.append(" ".join(cur))
            cur, cur_len = [], 0
    while cur:
        rest = []
        while len(cur) > 1 and cur[-1] in ARTICLES:
            rest.insert(0, cur.pop())
        lines.append(" ".join(cur))
        cur = rest
    return lines
