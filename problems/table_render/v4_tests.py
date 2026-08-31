import solution


def test_v4_returns_newline_joined_string():
    assert solution.render([["a", "bb"], ["ccc", "d"]]) == "a    bb\nccc  d"


def test_v4_empty_rows_empty_string():
    assert solution.render([]) == ""


def test_v4_alignment_and_separator_preserved():
    assert solution.render([["item", "qty"], ["apple", "5"], ["x", "-12"]]) == (
        "item   qty\napple    5\nx      -12"
    )


def test_v4_ragged_rows_in_single_string():
    assert solution.render([["x", "y"], ["longer"]]) == "x       y\nlonger"


def test_v4_single_row_has_no_newline():
    assert solution.render([["only"]]) == "only"
