import re

_ATX = re.compile(r"(#{1,6}) (.*)$")


def _atx_title(raw):
    title = raw.strip()
    trimmed = title.rstrip("#")
    if trimmed != title and (not trimmed or trimmed[-1] in " \t"):
        title = trimmed.rstrip()
    return title


def _slug_base(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def _with_slugs(raw_entries):
    counts = {}
    out = []
    for level, title in raw_entries:
        base = _slug_base(title)
        seen = counts.get(base, 0)
        counts[base] = seen + 1
        slug = base if seen == 0 else "%s-%d" % (base, seen + 1)
        out.append((level, title, slug))
    return out


def _scan(text):
    lines = text.splitlines()
    raw = []
    in_fence = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            in_fence = not in_fence
            i += 1
            continue
        if in_fence:
            i += 1
            continue
        m = _ATX.match(line)
        if m:
            raw.append((len(m.group(1)), _atx_title(m.group(2))))
            i += 1
            continue
        if line.strip() and i + 1 < len(lines):
            underline = lines[i + 1]
            if len(underline) >= 3 and set(underline) in ({"="}, {"-"}):
                level = 1 if underline[0] == "=" else 2
                raw.append((level, line.strip()))
                i += 2
                continue
        i += 1
    return raw


def toc(text):
    roots = []
    stack = []
    for level, title, slug in _with_slugs(_scan(text)):
        node = {"title": title, "slug": slug, "level": level, "children": []}
        while stack and stack[-1]["level"] >= level:
            stack.pop()
        if stack:
            stack[-1]["children"].append(node)
        else:
            roots.append(node)
        stack.append(node)
    return roots
