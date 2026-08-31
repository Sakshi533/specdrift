import solution


def test_v1_shorter_component_list_can_win():
    assert solution.cmp("1.2.10", "1.3") == -1


def test_v1_missing_components_are_zero():
    assert solution.cmp("1.2", "1.2.0") == 0


def test_v1_numeric_not_lexicographic():
    assert solution.cmp("1.10", "1.9") == 1


def test_v1_leading_zeros_ignored():
    assert solution.cmp("1.02", "1.2") == 0


def test_v1_returns_sign_triple():
    assert solution.cmp("0.9", "1.0") == -1
    assert solution.cmp("1.0", "0.9") == 1
    assert solution.cmp("3", "3.0.0") == 0
