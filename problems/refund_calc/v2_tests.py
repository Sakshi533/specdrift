import solution


def test_v1_full_refund_when_recent():
    assert solution.refund(2000, 3, False) == 2000


def test_v1_half_refund_floors_in_second_tier():
    assert solution.refund(999, 20, False) == 499


def test_v1_no_refund_after_thirty_days():
    assert solution.refund(5000, 45, False) == 0


def test_v1_opened_after_thirty_days_still_zero():
    assert solution.refund(4000, 60, True) == 0


def test_v2_restocking_fee_comes_off_after_halving():
    # tier 3000, halved 1500, minus 500
    assert solution.refund(3000, 10, True) == 1000


def test_v2_fee_clamps_refund_at_zero():
    # tier 500, halved 250, minus 500 -> clamped to 0
    assert solution.refund(1001, 20, True) == 0


def test_v2_small_opened_refund_goes_to_zero():
    # tier 400, halved 200, minus 500 -> clamped to 0
    assert solution.refund(400, 3, True) == 0


def test_v2_unopened_items_pay_no_fee():
    assert solution.refund(3000, 10, False) == 3000
