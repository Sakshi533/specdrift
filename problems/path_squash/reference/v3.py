def squash(path):
    if ".." in path.split("/"):
        raise ValueError("'..' segments are not allowed")
    absolute = path.startswith("/")
    parts = [p for p in path.split("/") if p not in ("", ".")]
    joined = "/".join(parts)
    return "/" + joined if absolute else joined
