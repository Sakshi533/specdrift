import solution


def test_v1_collapses_repeated_slashes():
    assert solution.squash("a//b///c") == "a/b/c"


def test_v1_removes_dot_segments():
    assert solution.squash("./a/./b/.") == "a/b"


def test_v1_absolute_stays_absolute_without_trailing_slash():
    assert solution.squash("/a//b/") == "/a/b"


def test_v1_root_stays_root():
    assert solution.squash("/") == "/"


def test_v1_dotdot_left_as_is():
    assert solution.squash("a/../b") == "a/../b"
