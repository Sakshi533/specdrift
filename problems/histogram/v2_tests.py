import solution


def test_v2_interior_values_with_under_and_over():
    assert solution.bins([-3, 1, 2, 7, 12], [0, 5, 10]) == (1, [2, 1], 1)


def test_v2_left_edge_in_bin_right_edge_is_over():
    # 0 -> bin 0, 5 -> bin 1, 10 -> over
    assert solution.bins([0, 5, 10], [0, 5, 10]) == (0, [1, 1], 1)


def test_v2_all_under_and_over():
    assert solution.bins([-5, -4, 11], [0, 10]) == (2, [0], 1)


def test_v2_empty_values():
    assert solution.bins([], [0, 3]) == (0, [0], 0)


def test_v2_single_bin_interior_value():
    assert solution.bins([2], [1, 4]) == (0, [1], 0)
