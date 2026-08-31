import solution


def test_v1_nearest_car_wins():
    assert solution.pick([(0, "idle"), (5, "idle"), (9, "idle")], 6) == 1


def test_v1_tie_between_idle_cars_lowest_index():
    assert solution.pick([(2, "idle"), (6, "idle")], 4) == 0


def test_v1_tie_lowest_index_beats_idleness():
    # pure index tiebreak: the moving car at index 0 wins the tie
    assert solution.pick([(3, "up"), (7, "idle")], 5) == 0


def test_v1_car_at_the_floor_wins():
    assert solution.pick([(7, "up"), (3, "idle")], 3) == 1


def test_v1_toward_moving_car_wins_by_distance():
    assert solution.pick([(10, "down"), (2, "up")], 8) == 0
