def parse(text):
    data = {}
    current = ""
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line[0] in ";#":
            continue
        if line.startswith("[") and line.endswith("]"):
            current = line[1:-1].strip()
            data.setdefault(current, {})
            continue
        if "=" in line:
            key, _, value = line.partition("=")
            section = data.setdefault(current, {})
            key = key.strip()
            if key not in section:
                section[key] = value.strip()
    return data
