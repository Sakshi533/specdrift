ONE_LARGER = {"S": "M", "M": "L"}


def assign(spots, cars):
    free = [True] * len(spots)
    out = []
    for vehicle in cars:
        if vehicle == "XS":
            wants = ("S", "M", "L")   # smallest free size wins
        else:
            wants = tuple(w for w in (vehicle, ONE_LARGER.get(vehicle)) if w)
        idx = -1
        for want in wants:
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
