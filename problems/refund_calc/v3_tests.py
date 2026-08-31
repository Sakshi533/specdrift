import solution


def test_v1_full_refund_when_recent():
    assert solution.refund(2000, 3, False) == 2000


def test_v1_half_refund_floors_in_second_tier():
    assert solution.refund(999, 20, False) == 499


def test_v1_no_refund_after_thirty_days():
    assert solution.refund(5000, 45, False) == 0


def test_v1_opened_after_thirty_days_still_zero():
    assert solution.refund(4000, 60, True) == 0


def test_v2_fee_clamps_refund_at_zero():
    # tier 500: fee eats it under either order -> 0
    assert solution.refund(1001, 20, True) == 0


def test_v2_small_opened_refund_goes_to_zero():
    # tier 400: fee eats it under either order -> 0
    assert solution.refund(400, 3, True) == 0


def test_v2_unopened_items_pay_no_fee():
    assert solution.refund(3000, 10, False) == 3000


def test_v3_fee_comes_off_before_halving():
    # tier 3000, minus 500 = 2500, halved -> 1250 (not 1500 // 2 - ... = 1000)
    assert solution.refund(3000, 10, True) == 1250


def test_v3_order_matters_in_second_tier():
    # tier 1000, minus 500 = 500, halved -> 250 (old order gave 0)
    assert solution.refund(2000, 20, True) == 250


def test_v3_small_tier_survives_new_order():
    # tier 600, minus 500 = 100, halved -> 50 (old order gave 0)
    assert solution.refund(600, 10, True) == 50
