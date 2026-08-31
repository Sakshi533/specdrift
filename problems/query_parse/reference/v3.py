def _decode(s):
    out = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "%" and i + 2 < len(s):
            out.append(chr(int(s[i + 1:i + 3], 16)))
            i += 3
        elif ch == "+":
            out.append(" ")
            i += 1
        else:
            out.append(ch)
            i += 1
    return "".join(out)


def parse(qs):
    if qs == "":
        return {}
    out = {}
    for segment in qs.split("&"):
        key, _, value = segment.partition("=")
        out.setdefault(_decode(key), []).append(_decode(value))
    return out
