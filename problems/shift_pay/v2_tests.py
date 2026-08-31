import solution


def test_v1_single_shift_paid_at_flat_rate():
    assert solution.pay([(540, 1020)], 10) == 4800


def test_v1_minutes_beyond_2400_paid_time_and_a_half():
    shifts = [(480, 960), (1920, 2400), (3360, 3840), (4800, 5280), (6240, 6720), (7680, 7780)]
    # 2400 regular + 100 overtime at rate 10
    assert solution.pay(shifts, 10) == 25500


def test_v1_overtime_term_floors_once():
    shifts = [(480, 960), (1920, 2400), (3360, 3840), (4800, 5280), (6240, 6720), (7680, 7681)]
    # 2400 * 7 + (1 * 7 * 3) // 2 = 16800 + 10
    assert solution.pay(shifts, 7) == 16810


def test_v1_disjoint_shifts_sum():
    assert solution.pay([(0, 120), (300, 420)], 25) == 6000


def test_v2_night_window_earns_quarter_bonus():
    # 120 night minutes at rate 8: base 960 + 240
    assert solution.pay([(1320, 1440)], 8) == 1200


def test_v2_shift_spanning_midnight_splits_night_minutes():
    # minutes 1380-1439 are night, 1440-1499 are day-1 morning: base 1200 + 60 * 10 // 4
    assert solution.pay([(1380, 1500)], 10) == 1350


def test_v2_night_bonus_floors_once_over_all_night_minutes():
    # 3 night minutes at rate 6: bonus is 3 * 6 // 4 = 4, not 3 * (6 // 4) = 3
    assert solution.pay([(1437, 1440)], 6) == 22


def test_v2_night_and_daytime_overtime_are_separate_bonuses():
    # 120 night minutes early in the week; the 120 overtime minutes all fall in daytime
    shifts = [(1320, 1440), (1920, 2400), (3360, 3840), (4800, 5280), (6240, 6720), (7680, 8160)]
    # base 2520 * 4 + night 120 * 4 // 4 + overtime 120 * 4 // 2
    assert solution.pay(shifts, 4) == 10440
