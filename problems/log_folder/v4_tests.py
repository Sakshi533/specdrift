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


def test_v2_nonadjacent_not_collapsed():
    assert solution.fold(["a", "b", "a"]) == ["a", "b", "a"]


def test_v3_adjacent_identical_collapse():
    assert solution.fold(["ping", "ping"]) == ["2 x ping"]


def test_v3_collapse_counts_after_folding():
    lines = ["e", "  x", "e", "  x", "e", "  x"]
    assert solution.fold(lines) == ["3 x e x"]


def test_v3_singleton_gets_no_prefix():
    assert solution.fold(["q", "q", "r"]) == ["2 x q", "r"]


def test_v3_prefix_lookalike_line_untouched():
    assert solution.fold(["2 x q"]) == ["2 x q"]


def test_v4_empty_strings_produce_no_output():
    assert solution.fold(["a", "", "b"]) == ["a", "b"]


def test_v4_empty_string_breaks_continuation():
    assert solution.fold(["a", "", "   b"]) == ["a", "b"]


def test_v4_collapse_reaches_across_removed_empties():
    assert solution.fold(["x", "", "x"]) == ["2 x x"]


def test_v4_all_empty_input():
    assert solution.fold(["", ""]) == []


def test_v4_none_entry_raises():
    try:
        solution.fold(["ok", None])
    except ValueError:
        pass
    else:
        assert False, "expected ValueError for a None entry"
