def squash(path):
    path = path.strip()
    if ".." in path.split("/"):
        raise ValueError("'..' segments are not allowed")
    absolute = path.startswith("/")
    parts = [p for p in path.split("/") if p not in ("", ".")]
    if not parts:
        return "/" if absolute else "."
    joined = "/".join(parts)
    return "/" + joined if absolute else joined
