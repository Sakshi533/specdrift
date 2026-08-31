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


def test_v2_integer_cells_right_aligned():
    assert solution.render([["item", "qty"], ["apple", "5"]]) == [
        "item  | qty",
        "apple |   5",
    ]


def test_v2_negative_integer_right_aligned():
    assert solution.render([["n"], ["-12"], ["3"]]) == ["n", "-12", "  3"]


def test_v2_mixed_alignment_per_cell():
    assert solution.render([["num", "note"], ["42", "ok"], ["x", "1.5"]]) == [
        "num | note",
        " 42 | ok",
        "x   | 1.5",
    ]


def test_v2_dash_alone_is_not_an_integer():
    assert solution.render([["-", "aaa"], ["bb", "c"]]) == ["-  | aaa", "bb | c"]
