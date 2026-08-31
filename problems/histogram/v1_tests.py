import solution


def test_v1_basic_counts():
    assert solution.bins([1, 2, 7, 7, 9], [0, 5, 10]) == [2, 3]


def test_v1_left_edge_in_right_edge_out():
    # 0 -> bin 0, 5 -> bin 1, 10 -> outside
    assert solution.bins([0, 5, 10], [0, 5, 10]) == [1, 1]


def test_v1_values_outside_all_bins_ignored():
    assert solution.bins([-3, 12], [0, 5, 10]) == [0, 0]


def test_v1_empty_values():
    assert solution.bins([], [0, 3]) == [0]
