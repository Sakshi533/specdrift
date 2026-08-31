def format_phone(digits):
    cleaned = "".join(c for c in digits if c not in " -.()")
    if len(cleaned) == 11 and cleaned.startswith("1") and cleaned.isdigit():
        cleaned = cleaned[1:]
    if len(cleaned) != 10 or not cleaned.isdigit():
        return None
    return "({}) {}-{}".format(cleaned[:3], cleaned[3:6], cleaned[6:])
