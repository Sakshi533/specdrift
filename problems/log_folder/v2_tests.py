import solution


def test_v1_basic_fold():
    lines = ["ERROR boom", "    at foo()", "\tat bar()"]
    assert solution.fold(lines) == ["ERROR boom at foo() at bar()"]


def test_v1_plain_lines_untouched():
    assert solution.fold(["alpha", "beta"]) == ["alpha", "beta"]


def test_v1_leading_continuation_stands_alone():
    assert solution.fold(["   orphan", "next"]) == ["orphan", "next"]


def test_v1_inner_whitespace_preserved():
    assert solution.fold(["head", "  \t tail   spaced"]) == ["head tail   spaced"]


def test_v1_multiple_groups():
    lines = ["a", "  1", "b", "  2", "  3"]
    assert solution.fold(lines) == ["a 1", "b 2 3"]


def test_v2_adjacent_identical_collapse():
    assert solution.fold(["ping", "ping"]) == ["ping (x2)"]


def test_v2_collapse_counts_after_folding():
    lines = ["e", "  x", "e", "  x", "e", "  x"]
    assert solution.fold(lines) == ["e x (x3)"]


def test_v2_nonadjacent_not_collapsed():
    assert solution.fold(["a", "b", "a"]) == ["a", "b", "a"]


def test_v2_singleton_gets_no_suffix():
    assert solution.fold(["q", "q", "r"]) == ["q (x2)", "r"]
