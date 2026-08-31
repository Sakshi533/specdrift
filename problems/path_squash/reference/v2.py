def squash(path):
    absolute = path.startswith("/")
    out = []
    for p in path.split("/"):
        if p in ("", "."):
            continue
        if p == "..":
            if out and out[-1] != "..":
                out.pop()
            elif not absolute:
                out.append("..")
            # ".." above root is clamped away
        else:
            out.append(p)
    joined = "/".join(out)
    return "/" + joined if absolute else joined
