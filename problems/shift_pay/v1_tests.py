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
