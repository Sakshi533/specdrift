import solution


def test_v1_nearest_car_wins():
    assert solution.pick([(0, "idle"), (5, "idle"), (9, "idle")], 6) == 1


def test_v1_tie_between_idle_cars_lowest_index():
    assert solution.pick([(2, "idle"), (6, "idle")], 4) == 0


def test_v1_car_at_the_floor_wins():
    assert solution.pick([(7, "up"), (3, "idle")], 3) == 1


def test_v1_toward_moving_car_wins_by_distance():
    assert solution.pick([(10, "down"), (2, "up")], 8) == 0


def test_v2_away_car_no_longer_eligible():
    # index 0 is nearest but heading away; the far toward-mover gets the call
    assert solution.pick([(6, "up"), (1, "up")], 5) == 1


def test_v2_nearest_among_eligible_only():
    assert solution.pick([(6, "up"), (3, "idle"), (1, "up")], 5) == 1


def test_v2_lone_away_car_still_serves():
    assert solution.pick([(9, "up")], 4) == 0


def test_v2_all_away_falls_back_to_old_rule():
    assert solution.pick([(8, "up"), (2, "down")], 5) == 0


def test_v3_idle_beats_moving_on_tie():
    # rewrites the v1 tiebreak: the idle car at index 1 now wins the tie
    assert solution.pick([(3, "up"), (7, "idle")], 5) == 1


def test_v3_idle_wins_tie_even_at_higher_index():
    assert solution.pick([(2, "up"), (6, "idle"), (10, "idle")], 4) == 1


def test_v3_moving_tie_still_lowest_index():
    assert solution.pick([(4, "up"), (6, "down")], 5) == 0


def test_v3_distance_still_beats_idleness():
    # a strictly nearer moving car outranks a farther idle one
    assert solution.pick([(4, "up"), (8, "idle")], 5) == 0
