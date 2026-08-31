import re

_ATX = re.compile(r"(#{1,6}) (.*)$")


def _atx_title(raw):
    title = raw.strip()
    trimmed = title.rstrip("#")
    if trimmed != title and (not trimmed or trimmed[-1] in " \t"):
        title = trimmed.rstrip()
    return title


def toc(text):
    entries = []
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = _ATX.match(line)
        if m:
            entries.append((len(m.group(1)), _atx_title(m.group(2))))
    return entries
