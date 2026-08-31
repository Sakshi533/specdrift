import solution


def test_v4_returns_dict_with_deltas():
    assert solution.update(1200, 1200, "a") == {
        "a": 1216, "b": 1184, "delta_a": 16, "delta_b": -16}


def test_v4_draw_has_zero_deltas():
    assert solution.update(1500, 1500, "draw") == {
        "a": 1500, "b": 1500, "delta_a": 0, "delta_b": 0}


def test_v4_both_provisional_k64_breakdown():
    assert solution.update(900, 900, "a") == {
        "a": 932, "b": 868, "delta_a": 32, "delta_b": -32}


def test_v4_mixed_pair_average_k_zero_sum_breakdown():
    assert solution.update(950, 1200, "a") == {
        "a": 989, "b": 1161, "delta_a": 39, "delta_b": -39}


def test_v4_favorite_loss_breakdown():
    assert solution.update(1200, 1000, "b") == {
        "a": 1176, "b": 1024, "delta_a": -24, "delta_b": 24}


def test_v4_half_up_rounding_survives_in_deltas():
    assert solution.update(1000, 1275, "a") == {
        "a": 1027, "b": 1248, "delta_a": 27, "delta_b": -27}
