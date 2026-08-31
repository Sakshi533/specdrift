def pick(cars, floor):
    def away(pos, direction):
        return ((direction == "up" and pos > floor)
                or (direction == "down" and pos < floor))

    eligible = [i for i, (pos, d) in enumerate(cars) if not away(pos, d)]
    pool = eligible if eligible else list(range(len(cars)))
    return min(pool, key=lambda i: (abs(cars[i][0] - floor),
                                    0 if cars[i][1] == "idle" else 1, i))
