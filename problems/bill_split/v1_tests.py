import solution


def test_v1_earlier_people_get_extra_cents():
    assert solution.split(100, 3) == [34, 33, 33]


def test_v1_even_split_is_flat():
    assert solution.split(1000, 4) == [250, 250, 250, 250]


def test_v1_many_leftover_cents_go_to_front():
    assert solution.split(7, 5) == [2, 2, 1, 1, 1]


def test_v1_total_smaller_than_group():
    assert solution.split(5, 8) == [1, 1, 1, 1, 1, 0, 0, 0]
