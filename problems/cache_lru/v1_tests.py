import solution


def test_v1_get_returns_put_value():
    assert solution.trace(2, [("put", "a", 1), ("get", "a")]) == [1]


def test_v1_get_miss_returns_none():
    assert solution.trace(2, [("get", "x")]) == [None]


def test_v1_eviction_removes_least_recent():
    ops = [("put", "a", 1), ("put", "b", 2), ("put", "c", 3),
           ("get", "a"), ("get", "b"), ("get", "c")]
    assert solution.trace(2, ops) == [None, 2, 3]


def test_v1_get_hit_refreshes_recency():
    # get "a" makes it most-recent, so put "c" evicts "b" instead
    ops = [("put", "a", 1), ("put", "b", 2), ("get", "a"), ("put", "c", 3),
           ("get", "b"), ("get", "c")]
    assert solution.trace(2, ops) == [1, None, 3]


def test_v1_put_existing_refreshes_recency():
    # updating "a" makes it most-recent, so put "c" evicts "b"
    ops = [("put", "a", 1), ("put", "b", 2), ("put", "a", 9), ("put", "c", 3),
           ("get", "a"), ("get", "b")]
    assert solution.trace(2, ops) == [9, None]
