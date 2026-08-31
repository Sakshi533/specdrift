import solution


def test_v1_higher_priority_first():
    assert solution.order([("a", 1), ("b", 5), ("c", 3)]) == ["b", "c", "a"]


def test_v1_fifo_within_equal_priority():
    assert solution.order([("a", 2), ("b", 2), ("c", 2)]) == ["a", "b", "c"]


def test_v1_mixed_priorities_and_fifo():
    jobs = [("a", 1), ("b", 3), ("c", 3), ("d", 1)]
    assert solution.order(jobs) == ["b", "c", "a", "d"]


def test_v1_single_job():
    assert solution.order([("solo", 7)]) == ["solo"]
