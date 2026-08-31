import solution


def test_v1_full_refund_when_recent():
    assert solution.refund(2000, 3, False) == 2000


def test_v1_half_refund_floors_in_second_tier():
    assert solution.refund(999, 20, False) == 499


def test_v1_no_refund_after_thirty_days():
    assert solution.refund(5000, 45, False) == 0


def test_v1_opened_halves_the_tier_refund():
    assert solution.refund(1000, 10, True) == 500


def test_v1_opened_after_thirty_days_still_zero():
    assert solution.refund(4000, 60, True) == 0
