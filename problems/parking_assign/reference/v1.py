ONE_LARGER = {"S": "M", "M": "L"}


def assign(spots, cars):
    free = [True] * len(spots)
    out = []
    for car in cars:
        idx = -1
        for want in (car, ONE_LARGER.get(car)):
            if want is None:
                break
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
