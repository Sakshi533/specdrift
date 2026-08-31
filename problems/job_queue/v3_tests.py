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


def test_v2_eighth_slot_ages_again():
    jobs = [("h1", 9), ("h2", 9), ("h3", 9), ("l1", 1), ("h4", 9),
            ("h5", 9), ("h6", 9), ("l2", 1), ("h7", 9)]
    assert solution.order(jobs) == ["h1", "h2", "h3", "l1", "h4",
                                    "h5", "h6", "l2", "h7"]


def test_v3_aging_targets_lowest_tier():
    # rewrites the v2 rule: slot 4 now jumps z (lowest tier), not m
    # (earliest-submitted lower job)
    jobs = [("a", 5), ("m", 3), ("b", 5), ("z", 1), ("c", 5), ("d", 5)]
    assert solution.order(jobs) == ["a", "b", "c", "z", "d", "m"]


def test_v3_fifo_within_lowest_tier():
    jobs = [("a", 5), ("z1", 1), ("b", 5), ("z2", 1), ("c", 5), ("d", 5)]
    assert solution.order(jobs) == ["a", "b", "c", "z1", "d", "z2"]


def test_v3_mid_tier_served_once_it_is_lowest():
    # slot 4 jumps z (tier 1); by slot 8 the lowest waiting tier is m's
    jobs = [("a", 9), ("b", 9), ("c", 9), ("m", 5), ("z", 1),
            ("d", 9), ("e", 9), ("f", 9), ("g", 9)]
    assert solution.order(jobs) == ["a", "b", "c", "z", "d",
                                    "e", "f", "m", "g"]
