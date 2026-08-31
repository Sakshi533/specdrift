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
