import solution


def test_v1_does_not_mutate_inputs():
    a, b = [3, 5], [1, 5, 7]
    solution.merge(a, b)
    assert a == [3, 5] and b == [1, 5, 7]


def test_v3_returns_value_source_pairs():
    assert solution.merge([1], [2]) == [(1, 'a'), (2, 'b')]


def test_v3_keeps_duplicates_with_tags():
    out = solution.merge([2, 2], [2])
    assert sorted(out) == [(2, 'a'), (2, 'a'), (2, 'b')]


def test_v3_sorted_by_value_ties_a_first():
    out = solution.merge([1, 3], [1, 2, 3])
    assert out == [(1, 'a'), (1, 'b'), (2, 'b'), (3, 'a'), (3, 'b')]
