def squash(path):
    absolute = path.startswith("/")
    parts = [p for p in path.split("/") if p not in ("", ".")]
    joined = "/".join(parts)
    return "/" + joined if absolute else joined
