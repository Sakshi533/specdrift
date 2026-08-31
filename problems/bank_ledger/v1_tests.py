import solution


def test_v1_signed_txns_applied():
    assert solution.apply_txns(100, [50, -30, 20]) == 140


def test_v1_empty_txns_leaves_balance():
    assert solution.apply_txns(75, []) == 75
