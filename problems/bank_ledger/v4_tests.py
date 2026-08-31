import solution

# v4 changes the return shape, so every return-value constraint is rewritten
# here with origin 4 (see AUTHORING.md: origin = version that last rewrote it).


def test_v4_returns_balance_and_fees_tuple():
    assert solution.apply_txns(100, [-150]) == (-100, 50)


def test_v4_fees_accumulate():
    assert solution.apply_txns(0, [-10, -10]) == (-120, 100)


def test_v4_no_overdraft_means_zero_fees():
    assert solution.apply_txns(100, [50, -30, 20]) == (140, 0)


def test_v4_empty_txns_leaves_balance():
    assert solution.apply_txns(75, []) == (75, 0)


def test_v4_exactly_zero_charges_nothing():
    assert solution.apply_txns(50, [-50]) == (0, 0)
