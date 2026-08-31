import solution


def test_v1_single_column():
    assert solution.render([["x"], ["yy"]]) == ["x", "yy"]


def test_v1_empty_rows_list():
    assert solution.render([]) == []


def test_v2_negative_integer_right_aligned():
    assert solution.render([["n"], ["-12"], ["3"]]) == ["n", "-12", "  3"]


def test_v3_two_space_separator():
    assert solution.render([["a", "bb"], ["ccc", "d"]]) == ["a    bb", "ccc  d"]


def test_v3_ragged_rows_no_pipes():
    assert solution.render([["x", "y", "z"], ["long"]]) == ["x     y  z", "long"]


def test_v3_right_alignment_with_new_separator():
    assert solution.render([["item", "qty"], ["apple", "5"]]) == [
        "item   qty",
        "apple    5",
    ]


def test_v3_mixed_alignment_per_cell():
    assert solution.render([["num", "note"], ["42", "ok"], ["x", "1.5"]]) == [
        "num  note",
        " 42  ok",
        "x    1.5",
    ]
