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


def test_v2_per_key_limits():
    events = [(0, "a"), (1, "b"), (2, "a"), (3, "b")]
    assert solution.allow(events, 1, 10) == [True, True, False, False]


def test_v2_keys_independent_at_same_timestamp():
    assert solution.allow([(0, "a"), (0, "b")], 1, 10) == [True, True]


def test_v2_legacy_ints_still_accepted():
    assert solution.allow([0, 100], 1, 50) == [True, True]


def test_v2_legacy_and_keyed_do_not_share_quota():
    assert solution.allow([0, (1, "a"), 2], 1, 10) == [True, True, False]


def test_v3_denied_event_consumes_quota():
    # rewrites the v1 rule: the denied event at t=5 now counts against t=12
    assert solution.allow([0, 5, 12], 1, 10) == [True, False, False]


def test_v3_denial_chain_extends_lockout():
    # each denial refreshes the window, locking out events the original
    # allowed event alone would no longer block
    assert solution.allow([0, 8, 16, 25], 1, 10) == [True, False, False, False]


def test_v3_denied_consumption_is_per_key():
    events = [(0, "a"), (5, "a"), (12, "a"), (12, "b")]
    assert solution.allow(events, 1, 10) == [True, False, False, True]


def test_v3_denied_event_ages_out():
    # a denied event still stops counting once it leaves the window
    assert solution.allow([0, 5, 16], 1, 10) == [True, False, True]


def test_v4_same_timestamp_burst_piggybacks():
    events = [(5, "a"), (5, "a"), (5, "a")]
    assert solution.allow(events, 1, 10) == [True, True, True]


def test_v4_piggyback_consumes_no_extra_quota():
    # the second (5,"a") rides for free, so (9,"a") still fits under limit 2
    events = [(5, "a"), (5, "a"), (9, "a")]
    assert solution.allow(events, 2, 10) == [True, True, True]


def test_v4_denied_first_blocks_piggyback():
    # first event at (a,5) is denied, so the duplicate is judged (and denied)
    # on its own, and both still consume quota
    events = [(0, "a"), (5, "a"), (5, "a")]
    assert solution.allow(events, 1, 10) == [True, False, False]


def test_v4_piggyback_is_per_key():
    events = [(5, "a"), (5, "b"), (5, "a")]
    assert solution.allow(events, 1, 10) == [True, True, True]


def test_v4_legacy_same_timestamp_piggybacks():
    assert solution.allow([3, 3], 1, 10) == [True, True]
