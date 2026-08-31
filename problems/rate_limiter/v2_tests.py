import solution


def test_v1_under_limit_all_allowed():
    assert solution.allow([0, 100, 200], 2, 10) == [True, True, True]


def test_v1_burst_over_limit_denied():
    assert solution.allow([0, 1, 2], 2, 10) == [True, True, False]


def test_v1_window_left_edge_excluded():
    # window is half-open: an event exactly `window` seconds later is clear
    assert solution.allow([0, 10], 1, 10) == [True, True]


def test_v1_event_inside_window_denied():
    assert solution.allow([0, 9], 1, 10) == [True, False]


def test_v1_denied_event_does_not_consume():
    # the denied event at t=5 must not count against t=12
    assert solution.allow([0, 5, 12], 1, 10) == [True, False, True]


def test_v2_per_key_limits():
    events = [(0, "a"), (1, "b"), (2, "a"), (3, "b")]
    assert solution.allow(events, 1, 10) == [True, True, False, False]


def test_v2_keys_independent_at_same_timestamp():
    assert solution.allow([(0, "a"), (0, "b")], 1, 10) == [True, True]


def test_v2_legacy_ints_still_accepted():
    assert solution.allow([0, 100], 1, 50) == [True, True]


def test_v2_legacy_and_keyed_do_not_share_quota():
    assert solution.allow([0, (1, "a"), 2], 1, 10) == [True, True, False]
