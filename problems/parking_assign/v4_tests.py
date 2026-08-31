import solution


def test_v1_exact_size_first_free_index():
    assert solution.assign(["M", "S", "S"], ["S"]) == [1]


def test_v1_falls_back_one_size_larger():
    assert solution.assign(["S", "M"], ["S", "S"]) == [0, 1]


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


def test_v3_s_car_may_take_l_spot():
    # rewrites the v1 cap: with nothing smaller free, S parks in L
    assert solution.assign(["L"], ["S"]) == [0]


def test_v3_second_s_car_climbs_past_old_cap():
    assert solution.assign(["L", "M"], ["S", "S"]) == [1, 0]


def test_v3_small_car_can_starve_a_big_one():
    # the S car grabs the only L first; the L car that follows gets nothing
    assert solution.assign(["L"], ["S", "L"]) == [0, -1]


def test_v4_unknown_vehicle_size_raises():
    try:
        solution.assign(["S"], ["Q"])
    except ValueError:
        return
    assert False, "expected ValueError for vehicle size 'Q'"


def test_v4_unknown_spot_size_raises_before_parking():
    try:
        solution.assign(["S", "XL"], ["S"])
    except ValueError:
        return
    assert False, "expected ValueError for spot size 'XL'"


def test_v4_xs_spot_raises():
    try:
        solution.assign(["XS"], ["S"])
    except ValueError:
        return
    assert False, "expected ValueError for spot size 'XS'"


def test_v4_empty_spots_all_unassigned():
    assert solution.assign([], ["S", "XS"]) == [-1, -1]


def test_v4_empty_cars_returns_empty_list():
    assert solution.assign([], []) == []
    assert solution.assign(["S"], []) == []
