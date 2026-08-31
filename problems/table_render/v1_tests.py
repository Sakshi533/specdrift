import solution


def test_v1_left_align_and_pipe_separator():
    assert solution.render([["a", "bb"], ["ccc", "d"]]) == ["a   | bb", "ccc | d"]


def test_v1_ragged_rows_padded_with_empty_cells():
    assert solution.render([["x", "y", "z"], ["long"]]) == [
        "x    | y | z",
        "long |   |",
    ]


def test_v1_single_column():
    assert solution.render([["x"], ["yy"]]) == ["x", "yy"]


def test_v1_empty_rows_list():
    assert solution.render([]) == []


def test_v1_no_trailing_whitespace_after_short_last_cell():
    assert solution.render([["aa", "xx"], ["b", "y"]]) == ["aa | xx", "b  | y"]
