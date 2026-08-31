def parse(qs):
    if qs == "":
        return {}
    out = {}
    for segment in qs.split("&"):
        key, _, value = segment.partition("=")
        out[key] = value
    return out
