import solution


def test_v1_first_fit_basic():
    assert solution.assign([4, 6], [3, 3]) == [0, 1]


def test_v1_no_fit_gets_minus_one():
    assert solution.assign([2], [3, 2]) == [-1, 0]


def test_v1_capacity_decreases_as_parties_seat():
    assert solution.assign([4], [2, 2, 2]) == [0, 0, -1]


def test_v1_takes_first_row_that_fits():
    # row 0 fits, so the tighter row 1 is not considered
    assert solution.assign([10, 3], [3]) == [0]


def test_v1_exact_fit_fills_row():
    assert solution.assign([2, 4], [4, 2]) == [1, 0]


def test_v2_big_party_takes_emptiest_row():
    assert solution.assign([5, 9], [5]) == [1]


def test_v2_small_party_still_first_fit():
    assert solution.assign([4, 6], [2]) == [0]


def test_v2_emptiest_tie_takes_lowest_index():
    assert solution.assign([6, 6], [6]) == [0]


def test_v2_big_parties_interact_through_capacity():
    # first 5 takes row 1 (8 free), leaving row 0 the emptiest for the second
    assert solution.assign([6, 8], [5, 5]) == [1, 0]


def test_v2_size_four_is_still_first_fit():
    assert solution.assign([4, 9], [4]) == [0]
