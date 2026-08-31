def pick(cars, floor):
    return min(range(len(cars)),
               key=lambda i: (abs(cars[i][0] - floor), i))
