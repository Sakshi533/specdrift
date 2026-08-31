import solution


def test_v1_greedy_packing():
    assert solution.wrap("the quick brown fox jumps", 10) == [
        "the quick", "brown fox", "jumps"]


def test_v1_fits_one_line():
    assert solution.wrap("hello world", 11) == ["hello world"]


def test_v1_width_boundary():
    assert solution.wrap("abc def", 7) == ["abc def"]
    assert solution.wrap("abc def", 6) == ["abc", "def"]


def test_v1_long_word_overflows_own_line():
    assert solution.wrap("go extraordinary now", 6) == [
        "go", "extraordinary", "now"]
