import solution


def test_v1_basic_split():
    assert solution.split_row("a,b,c") == ["a", "b", "c"]


def test_v1_empty_fields_kept():
    assert solution.split_row("a,,c") == ["a", "", "c"]


def test_v1_single_field():
    assert solution.split_row("hello") == ["hello"]


def test_v1_keeps_whitespace():
    assert solution.split_row(" a , b ") == [" a ", " b "]


def test_v2_quoted_field_with_comma():
    assert solution.split_row('a,"b,c",d') == ["a", "b,c", "d"]


def test_v2_quotes_stripped():
    assert solution.split_row('"hello"') == ["hello"]


def test_v2_comma_and_spaces_inside_quotes():
    assert solution.split_row('"x, y",z') == ["x, y", "z"]


def test_v3_doubled_quote_is_literal():
    assert solution.split_row('"He said ""hi""",x') == ['He said "hi"', "x"]


def test_v3_field_of_just_escaped_quote():
    assert solution.split_row('""""') == ['"']


def test_v3_escaped_quotes_at_both_ends():
    assert solution.split_row('"""quoted""",x') == ['"quoted"', "x"]
