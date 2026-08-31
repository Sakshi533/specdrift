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


def test_v2_both_provisional_move_at_k64():
    assert solution.update(900, 900, "a") == (932, 868)


def test_v2_provisional_draw_uses_k64_both_sides():
    assert solution.update(800, 950, "draw") == (813, 937)


def test_v2_provisional_loss_at_k64():
    assert solution.update(900, 999, "b") == (877, 1022)


def test_v2_mixed_pair_each_side_uses_own_k():
    # A provisional (K=64) gains 52; B established (K=32) loses 26 — not zero-sum
    assert solution.update(950, 1200, "a") == (1002, 1174)
