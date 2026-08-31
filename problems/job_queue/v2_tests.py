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


def test_v2_fourth_slot_ages_a_low_job():
    jobs = [("a", 5), ("b", 5), ("c", 5), ("d", 5), ("e", 1)]
    assert solution.order(jobs) == ["a", "b", "c", "e", "d"]


def test_v2_uniform_priority_aging_slot_is_normal():
    jobs = [("a", 2), ("b", 2), ("c", 2), ("d", 2), ("e", 2)]
    assert solution.order(jobs) == ["a", "b", "c", "d", "e"]


def test_v2_aging_picks_earliest_submitted_lower_job():
    # slot 4: m (submitted before z) jumps, even though z's tier is lower
    jobs = [("a", 5), ("m", 3), ("b", 5), ("z", 1), ("c", 5), ("d", 5)]
    assert solution.order(jobs) == ["a", "b", "c", "m", "d", "z"]


def test_v2_eighth_slot_ages_again():
    jobs = [("h1", 9), ("h2", 9), ("h3", 9), ("l1", 1), ("h4", 9),
            ("h5", 9), ("h6", 9), ("l2", 1), ("h7", 9)]
    assert solution.order(jobs) == ["h1", "h2", "h3", "l1", "h4",
                                    "h5", "h6", "l2", "h7"]
