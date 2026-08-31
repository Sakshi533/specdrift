import re


def slugify(s):
    slug = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")
    if len(slug) > 30:
        words = slug.split("-")
        out = words[0][:30]
        for w in words[1:]:
            if len(out) + 1 + len(w) > 30:
                break
            out += "-" + w
        slug = out
    return slug if slug else "n-a"
