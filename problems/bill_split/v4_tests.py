import solution


def test_v1_earlier_people_get_extra_cents():
    assert solution.split(100, 3) == [34, 33, 33]


def test_v1_even_split_is_flat():
    assert solution.split(1000, 4) == [250, 250, 250, 250]


def test_v1_many_leftover_cents_go_to_front():
    assert solution.split(7, 5) == [2, 2, 1, 1, 1]


def test_v1_total_smaller_than_group():
    assert solution.split(5, 8) == [1, 1, 1, 1, 1, 0, 0, 0]


def test_v2_exact_proportional_split():
    assert solution.split(100, [1, 1, 2]) == [25, 25, 50]


def test_v2_int_arg_still_means_equal_weights():
    assert solution.split(10, 4) == [3, 3, 2, 2]


def test_v3_smallest_remainder_gets_leftover_cent():
    assert solution.split(103, [5, 3, 1]) == [58, 34, 11]


def test_v3_smallest_remainder_tie_goes_to_lowest_index():
    assert solution.split(100, [3, 2, 2]) == [42, 29, 29]


def test_v3_largest_remainder_now_served_last():
    assert solution.split(101, [2, 2, 1]) == [40, 40, 21]


def test_v3_four_way_with_tied_pair():
    assert solution.split(101, [3, 3, 2, 2]) == [30, 30, 21, 20]


def test_v4_zero_weight_skipped_by_leftover_distribution():
    # naive smallest-remainder gives the cent to the zero-weight person (rem 0)
    assert solution.split(101, [1, 0, 1]) == [51, 0, 50]


def test_v4_zero_weight_between_tied_positives():
    # floors [5, 0, 5], leftover cent must go to index 0, never to the zero
    assert solution.split(11, [3, 0, 3]) == [6, 0, 5]


def test_v4_zero_weight_gets_exactly_zero_cents():
    assert solution.split(5, [0, 2, 3]) == [0, 2, 3]


def test_v4_all_zero_weights_raise():
    try:
        solution.split(100, [0, 0])
    except ValueError:
        return
    assert False, "expected ValueError for all-zero weights"
