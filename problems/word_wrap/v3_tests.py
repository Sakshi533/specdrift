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
