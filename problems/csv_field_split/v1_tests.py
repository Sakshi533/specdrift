import solution


def test_v1_basic_split():
    assert solution.split_row("a,b,c") == ["a", "b", "c"]


def test_v1_empty_fields_kept():
    assert solution.split_row("a,,c") == ["a", "", "c"]


def test_v1_single_field():
    assert solution.split_row("hello") == ["hello"]


def test_v1_keeps_whitespace():
    assert solution.split_row(" a , b ") == [" a ", " b "]
