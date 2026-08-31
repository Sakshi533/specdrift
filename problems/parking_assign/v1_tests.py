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
