import re


def slugify(s):
    slug = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    if len(slug) <= 30:
        return slug
    words = slug.split("-")
    out = words[0][:30]
    for w in words[1:]:
        if len(out) + 1 + len(w) > 30:
            break
        out += "-" + w
    return out
