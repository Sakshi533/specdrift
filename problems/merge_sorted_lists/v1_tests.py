import solution


def test_v1_merges_in_sorted_order():
    out = solution.merge([1, 4, 9], [2, 3, 10])
    assert out == [1, 2, 3, 4, 9, 10]


def test_v1_keeps_duplicates_with_multiplicity():
    out = solution.merge([1, 2, 2, 5], [2, 5])
    assert out == [1, 2, 2, 2, 5, 5]


def test_v1_does_not_mutate_inputs():
    a, b = [3, 5], [1, 5, 7]
    solution.merge(a, b)
    assert a == [3, 5] and b == [1, 5, 7]
