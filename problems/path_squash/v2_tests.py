import solution


def test_v1_collapses_repeated_slashes():
    assert solution.squash("a//b///c") == "a/b/c"


def test_v1_removes_dot_segments():
    assert solution.squash("./a/./b/.") == "a/b"


def test_v1_absolute_stays_absolute_without_trailing_slash():
    assert solution.squash("/a//b/") == "/a/b"


def test_v1_root_stays_root():
    assert solution.squash("/") == "/"


def test_v2_dotdot_cancels_previous_segment():
    assert solution.squash("a/../b") == "b"


def test_v2_chained_dotdot():
    assert solution.squash("a/b/../../c") == "c"


def test_v2_leading_dotdot_kept_in_relative_path():
    assert solution.squash("../a") == "../a"


def test_v2_dotdot_above_root_clamps_to_root():
    assert solution.squash("/..") == "/"
