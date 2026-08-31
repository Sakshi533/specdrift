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
    # floors [57, 34, 11], remainders 2/9, 3/9, 4/9 -> the cent goes to index 0
    assert solution.split(103, [5, 3, 1]) == [58, 34, 11]


def test_v3_smallest_remainder_tie_goes_to_lowest_index():
    # floors [42, 28, 28], remainders 6/7, 4/7, 4/7 -> cents to index 1 then 2
    assert solution.split(100, [3, 2, 2]) == [42, 29, 29]


def test_v3_largest_remainder_now_served_last():
    # floors [40, 40, 20], remainders 2/5, 2/5, 1/5 -> the cent goes to index 2
    assert solution.split(101, [2, 2, 1]) == [40, 40, 21]


def test_v3_four_way_with_tied_pair():
    # floors [30, 30, 20, 20], remainders 3,3,2,2 (/10) -> cent to index 2
    assert solution.split(101, [3, 3, 2, 2]) == [30, 30, 21, 20]
