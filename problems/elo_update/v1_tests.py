import solution


def test_v1_equal_ratings_winner_takes_sixteen():
    assert solution.update(1200, 1200, "a") == (1216, 1184)


def test_v1_favorite_losing_costs_more():
    assert solution.update(1200, 1000, "b") == (1176, 1024)


def test_v1_underdog_win_pays_more():
    assert solution.update(1400, 1600, "a") == (1424, 1576)


def test_v1_equal_ratings_draw_changes_nothing():
    assert solution.update(1500, 1500, "draw") == (1500, 1500)


def test_v1_delta_rounds_half_up_not_truncated():
    # 32 * (1 - Ea) = 26.548... -> 27, truncation would give 26
    assert solution.update(1000, 1275, "a") == (1027, 1248)
