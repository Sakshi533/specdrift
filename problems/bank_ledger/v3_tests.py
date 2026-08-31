import solution


def test_v1_signed_txns_applied():
    assert solution.apply_txns(100, [50, -30, 20]) == 140


def test_v1_empty_txns_leaves_balance():
    assert solution.apply_txns(75, []) == 75


def test_v2_withdrawal_to_exactly_zero_applied():
    assert solution.apply_txns(50, [-50, 20]) == 20


def test_v3_overdraft_applied_with_fee():
    assert solution.apply_txns(100, [-150]) == -100  # -50 balance, then 50 fee


def test_v3_each_negative_txn_charged():
    assert solution.apply_txns(0, [-10, -10]) == -120  # -60 after first, -120 after second


def test_v3_no_fee_at_or_above_zero():
    assert solution.apply_txns(100, [-100, 60]) == 60


def test_v3_balance_can_recover_after_fee():
    assert solution.apply_txns(40, [-50, 200]) == 140  # -60 after fee, then +200
