FITS = {
    "XS": ("S", "M", "L"),
    "S": ("S", "M", "L"),
    "M": ("M", "L"),
    "L": ("L",),
}


def assign(spots, cars):
    free = [True] * len(spots)
    out = []
    for vehicle in cars:
        idx = -1
        for want in FITS[vehicle]:   # smallest fitting size first
            for i, size in enumerate(spots):
                if free[i] and size == want:
                    idx = i
                    break
            if idx != -1:
                break
        if idx != -1:
            free[idx] = False
        out.append(idx)
    return out
