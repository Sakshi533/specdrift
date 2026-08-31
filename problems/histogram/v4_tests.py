import solution


def test_v2_interior_values_with_under_and_over():
    assert solution.bins([-3, 1, 2, 7, 12], [0, 5, 10]) == (1, [2, 1], 1)


def test_v2_all_under_and_over():
    assert solution.bins([-5, -4, 11], [0, 10]) == (2, [0], 1)


def test_v2_empty_values():
    assert solution.bins([], [0, 3]) == (0, [0], 0)


def test_v2_single_bin_interior_value():
    assert solution.bins([2], [1, 4]) == (0, [1], 0)


def test_v3_shared_edge_value_falls_in_left_bin():
    assert solution.bins([5], [0, 5, 10]) == (0, [1, 0], 0)


def test_v3_first_edge_counts_as_under():
    assert solution.bins([0], [0, 5, 10]) == (1, [0, 0], 0)


def test_v3_last_edge_in_final_bin_not_over():
    assert solution.bins([10], [0, 5, 10]) == (0, [0, 1], 0)


def test_v3_over_is_strictly_above_last_edge():
    # 11 over, 10 in the bin, 0 and -1 under
    assert solution.bins([11, 10, 0, -1], [0, 10]) == (2, [1], 1)


def test_v4_zero_width_bin_captures_its_edge_value():
    # 5s go to the zero-width bin (5, 5), not to (0, 5]
    assert solution.bins([5, 5, 3], [0, 5, 5, 10]) == (0, [1, 2, 0], 0)


def test_v4_zero_width_bin_without_matches_counts_zero():
    assert solution.bins([2, 8], [0, 5, 5, 10]) == (0, [1, 0, 1], 0)


def test_v4_first_of_equal_zero_width_bins_wins():
    assert solution.bins([5], [0, 5, 5, 5, 10]) == (0, [0, 1, 0, 0], 0)


def test_v4_under_over_rules_beat_zero_width_capture():
    # 5 is <= edges[0] so it is under; 10 is not over, so the (10, 10) bin catches it
    assert solution.bins([5, 10], [5, 5, 10, 10]) == (1, [0, 0, 1], 0)
