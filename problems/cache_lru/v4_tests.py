import solution


# v4 changed the return shape, so every behavioral constraint below is
# re-pinned against the new dict interface (hence origin v4 throughout).

def test_v4_returns_stats_dict():
    out = solution.trace(2, [("put", "a", 1), ("get", "a"), ("get", "b")])
    assert out == {"results": [1, None], "evicted": [], "hits": 1, "misses": 1}


def test_v4_evicted_keys_in_order():
    ops = [("put", "a", 1), ("put", "b", 2), ("put", "c", 3), ("put", "d", 4)]
    out = solution.trace(2, ops)
    assert out == {"results": [], "evicted": ["a", "b"], "hits": 0, "misses": 0}


def test_v4_peek_counts_toward_hits_and_misses():
    ops = [("put", "a", 1), ("peek", "a"), ("peek", "x")]
    out = solution.trace(2, ops)
    assert out == {"results": [1, None], "evicted": [], "hits": 1, "misses": 1}


def test_v4_put_existing_still_keeps_position():
    ops = [("put", "a", 1), ("put", "b", 2), ("put", "a", 9), ("put", "c", 3),
           ("get", "a"), ("get", "b"), ("get", "c")]
    out = solution.trace(2, ops)
    assert out == {"results": [None, 2, 3], "evicted": ["a"], "hits": 2, "misses": 1}


def test_v4_get_refresh_reflected_in_evictions():
    ops = [("put", "a", 1), ("put", "b", 2), ("get", "a"), ("put", "c", 3),
           ("get", "b")]
    out = solution.trace(2, ops)
    assert out == {"results": [1, None], "evicted": ["b"], "hits": 1, "misses": 1}


def test_v4_peek_still_does_not_refresh():
    ops = [("put", "a", 1), ("put", "b", 2), ("peek", "a"), ("put", "c", 3),
           ("get", "a"), ("get", "b")]
    out = solution.trace(2, ops)
    assert out == {"results": [1, None, 2], "evicted": ["a"], "hits": 2, "misses": 1}
