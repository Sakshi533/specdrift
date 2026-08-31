import solution


def test_v1_collapses_repeated_slashes():
    assert solution.squash("a//b///c") == "a/b/c"


def test_v1_removes_dot_segments():
    assert solution.squash("./a/./b/.") == "a/b"


def test_v1_absolute_stays_absolute_without_trailing_slash():
    assert solution.squash("/a//b/") == "/a/b"


def test_v1_root_stays_root():
    assert solution.squash("/") == "/"


def test_v3_dotdot_raises():
    try:
        solution.squash("a/../b")
    except ValueError:
        return
    assert False, "expected ValueError for 'a/../b'"


def test_v3_leading_dotdot_raises():
    try:
        solution.squash("../a")
    except ValueError:
        return
    assert False, "expected ValueError for '../a'"


def test_v3_dotdot_above_root_raises():
    try:
        solution.squash("/..")
    except ValueError:
        return
    assert False, "expected ValueError for '/..'"


def test_v3_dotted_names_are_not_traversal():
    assert solution.squash("a../..b/...") == "a../..b/..."
