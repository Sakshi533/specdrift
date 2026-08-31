import solution


def test_v1_first_fit_basic():
    assert solution.assign([4, 6], [3, 3]) == [0, 1]


def test_v1_no_fit_gets_minus_one():
    assert solution.assign([2], [3, 2]) == [-1, 0]


def test_v1_capacity_decreases_as_parties_seat():
    assert solution.assign([4], [2, 2, 2]) == [0, 0, -1]


def test_v1_exact_fit_fills_row():
    assert solution.assign([2, 4], [4, 2]) == [1, 0]


def test_v2_small_party_still_first_fit():
    assert solution.assign([4, 6], [2]) == [0]


def test_v2_emptiest_tie_takes_lowest_index():
    assert solution.assign([6, 6], [6]) == [0]


def test_v2_size_four_is_still_first_fit():
    assert solution.assign([4, 9], [4]) == [0]


def test_v3_best_fit_takes_fewest_leftover():
    # rewrites the v1 first-fit rule: the snug row 1 wins now
    assert solution.assign([10, 3], [3]) == [1]


def test_v3_big_party_best_fit_not_emptiest():
    # rewrites the v2 emptiest rule: leftover 0 beats leftover 4
    assert solution.assign([5, 9], [5]) == [0]


def test_v3_best_fit_tie_takes_lowest_index():
    assert solution.assign([5, 5], [3]) == [0]


def test_v3_best_fit_interacts_through_capacity():
    # first 5 now takes row 0 (leftover 1), pushing the second into row 1
    assert solution.assign([6, 8], [5, 5]) == [0, 1]


def test_v3_no_fit_still_minus_one():
    assert solution.assign([3, 4], [6, 4]) == [-1, 1]


def test_v4_zero_size_party_raises():
    try:
        solution.assign([4], [0])
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"


def test_v4_negative_size_party_raises():
    try:
        solution.assign([4, 4], [2, -1])
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"


def test_v4_empty_rows_skips_everyone():
    assert solution.assign([], [1, 2]) == [-1, -1]


def test_v4_empty_parties_returns_empty():
    assert solution.assign([5], []) == []
