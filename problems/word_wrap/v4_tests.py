import solution


def test_v1_greedy_packing():
    assert solution.wrap("the quick brown fox jumps", 10) == [
        "the quick", "brown fox", "jumps"]


def test_v1_fits_one_line():
    assert solution.wrap("hello world", 11) == ["hello world"]


def test_v1_width_boundary():
    assert solution.wrap("abc def", 7) == ["abc def"]
    assert solution.wrap("abc def", 6) == ["abc", "def"]


def test_v3_long_word_overflows_again():
    assert solution.wrap("go extraordinary now", 6) == [
        "go", "extraordinary", "now"]


def test_v3_article_a_moved_down():
    assert solution.wrap("she saw a bird", 9) == ["she saw", "a bird"]


def test_v3_article_the_moved_down():
    assert solution.wrap("we walked the dog", 13) == ["we walked", "the dog"]


def test_v3_final_line_never_ends_with_article():
    assert solution.wrap("look at the", 11) == ["look at", "the"]


def test_v3_lone_article_line_allowed():
    assert solution.wrap("a bb", 2) == ["a", "bb"]


def test_v4_empty_text_returns_empty_list():
    assert solution.wrap("", 5) == []


def test_v4_whitespace_only_returns_empty_list():
    assert solution.wrap("  \t  ", 5) == []


def test_v4_zero_width_raises():
    try:
        solution.wrap("hello", 0)
    except ValueError:
        pass
    else:
        assert False, "expected ValueError for width 0"


def test_v4_negative_width_raises():
    try:
        solution.wrap("hello world", -3)
    except ValueError:
        pass
    else:
        assert False, "expected ValueError for negative width"
