def _parse(v):
    base, sep, tag = v.partition("-")
    nums = [int(c) for c in base.split(".")]
    return nums, (tag if sep else None)


def cmp(a, b):
    na, ta = _parse(a)
    nb, tb = _parse(b)
    n = max(len(na), len(nb))
    na += [0] * (n - len(na))
    nb += [0] * (n - len(nb))
    if na != nb:
        return -1 if na < nb else 1
    if ta is None and tb is None:
        return 0
    if ta is None:
        return 1  # release sorts after any pre-release
    if tb is None:
        return -1
    if ta == tb:
        return 0
    return -1 if ta < tb else 1
