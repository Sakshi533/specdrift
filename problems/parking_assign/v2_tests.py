import solution


def test_v1_exact_size_first_free_index():
    assert solution.assign(["M", "S", "S"], ["S"]) == [1]


def test_v1_falls_back_one_size_larger():
    assert solution.assign(["S", "M"], ["S", "S"]) == [0, 1]


def test_v1_s_car_cannot_take_l_spot():
    # fallback is capped at one size up
    assert solution.assign(["L"], ["S"]) == [-1]


def test_v1_l_car_has_no_fallback():
    assert solution.assign(["M"], ["L"]) == [-1]


def test_v1_spots_stay_taken():
    assert solution.assign(["S", "S", "M"], ["S", "S", "S"]) == [0, 1, 2]


def test_v2_xs_prefers_s_spot_over_earlier_m():
    assert solution.assign(["M", "S"], ["XS"]) == [1]


def test_v2_xs_falls_through_m_to_l():
    assert solution.assign(["L", "M"], ["XS", "XS", "XS"]) == [1, 0, -1]


def test_v2_xs_fills_s_spots_by_index():
    assert solution.assign(["M", "S", "S"], ["XS", "XS"]) == [1, 2]


def test_v2_xs_competes_with_cars_for_spots():
    # the motorcycle takes the only S, pushing the S car up to the M spot
    assert solution.assign(["S", "M"], ["XS", "S"]) == [0, 1]
