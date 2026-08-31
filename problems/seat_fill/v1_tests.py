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
