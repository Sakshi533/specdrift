import solution


def test_v4_returns_breakdown_dict():
    assert solution.pay([(540, 1020)], 10) == {
        "total": 4800, "base": 4800, "night_bonus": 0, "overtime_bonus": 0}


def test_v4_overtime_only_breakdown():
    shifts = [(480, 960), (1920, 2400), (3360, 3840), (4800, 5280), (6240, 6720), (7680, 7780)]
    assert solution.pay(shifts, 10) == {
        "total": 25500, "base": 25000, "night_bonus": 0, "overtime_bonus": 500}


def test_v4_night_only_breakdown():
    assert solution.pay([(1320, 1440)], 8) == {
        "total": 1200, "base": 960, "night_bonus": 240, "overtime_bonus": 0}


def test_v4_disjoint_night_and_overtime_both_appear():
    shifts = [(1320, 1440), (1920, 2400), (3360, 3840), (4800, 5280), (6240, 6720), (7680, 8160)]
    assert solution.pay(shifts, 4) == {
        "total": 10440, "base": 10080, "night_bonus": 120, "overtime_bonus": 240}


def test_v4_overlapping_night_overtime_still_does_not_stack():
    shifts = [(480, 960), (1920, 2400), (3360, 3840), (4800, 5280), (6240, 6720), (8520, 8640)]
    assert solution.pay(shifts, 8) == {
        "total": 20640, "base": 20160, "night_bonus": 0, "overtime_bonus": 480}


def test_v4_split_night_shift_breakdown():
    shifts = [(480, 960), (1920, 2400), (3360, 3840), (4800, 5280), (6240, 6660), (8520, 8640)]
    assert solution.pay(shifts, 12) == {
        "total": 30060, "base": 29520, "night_bonus": 180, "overtime_bonus": 360}
