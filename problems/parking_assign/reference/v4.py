SPOT_SIZES = {"S", "M", "L"}
FITS = {
    "XS": ("S", "M", "L"),
    "S": ("S", "M", "L"),
    "M": ("M", "L"),
    "L": ("L",),
}


def assign(spots, cars):
    for size in spots:
        if size not in SPOT_SIZES:
            raise ValueError(f"invalid spot size: {size!r}")
    for vehicle in cars:
        if vehicle not in FITS:
            raise ValueError(f"invalid vehicle size: {vehicle!r}")
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
