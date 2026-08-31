from itertools import groupby


def _runs(tag):
    # numeric runs sort before alpha runs at the same position, so kind 0 < kind 1
    return [(0, int(text)) if is_num else (1, text)
            for is_num, text in
            ((k, "".join(g)) for k, g in groupby(tag, key=str.isdigit))]


def _parse(v):
    base, sep, tag = v.partition("-")
    nums = [int(c) for c in base.split(".")]
    return nums, (_runs(tag) if sep else None)


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
