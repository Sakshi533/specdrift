import solution


# v4 changed the return shape, so every behavioral constraint below is
# re-pinned against the (name, wait) interface (hence origin v4 throughout).

def test_v4_returns_name_wait_pairs():
    assert solution.order([("a", 1), ("b", 5)]) == [("b", 0), ("a", 1)]


def test_v4_fifo_waits_within_equal_priority():
    assert solution.order([("a", 2), ("b", 2), ("c", 2)]) == \
        [("a", 0), ("b", 1), ("c", 2)]


def test_v4_single_job_waits_zero():
    assert solution.order([("solo", 7)]) == [("solo", 0)]


def test_v4_aging_slot_wait_numbers():
    jobs = [("a", 5), ("b", 5), ("c", 5), ("d", 5), ("e", 1)]
    assert solution.order(jobs) == \
        [("a", 0), ("b", 1), ("c", 2), ("e", 3), ("d", 4)]


def test_v4_lowest_tier_aging_wait_numbers():
    jobs = [("a", 5), ("m", 3), ("b", 5), ("z", 1), ("c", 5), ("d", 5)]
    assert solution.order(jobs) == \
        [("a", 0), ("b", 1), ("c", 2), ("z", 3), ("d", 4), ("m", 5)]
