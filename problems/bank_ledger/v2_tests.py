import solution


def test_v1_signed_txns_applied():
    assert solution.apply_txns(100, [50, -30, 20]) == 140


def test_v1_empty_txns_leaves_balance():
    assert solution.apply_txns(75, []) == 75


def test_v2_overdrawing_txn_skipped():
    assert solution.apply_txns(100, [-150, 30]) == 130


def test_v2_withdrawal_to_exactly_zero_applied():
    assert solution.apply_txns(50, [-50, 20]) == 20


def test_v2_processing_continues_after_skip():
    assert solution.apply_txns(10, [-20, -5]) == 5
