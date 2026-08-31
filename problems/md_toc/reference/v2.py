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


def toc(text):
    raw = []
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = _ATX.match(line)
        if m:
            raw.append((len(m.group(1)), _atx_title(m.group(2))))
    return _with_slugs(raw)
