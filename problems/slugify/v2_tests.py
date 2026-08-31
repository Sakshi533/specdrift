import solution


def test_v1_basic_words_to_hyphens():
    assert solution.slugify("hello world") == "hello-world"


def test_v1_lowercases():
    assert solution.slugify("Hello World") == "hello-world"


def test_v1_collapses_separator_runs():
    assert solution.slugify("a -- b!! c") == "a-b-c"


def test_v1_strips_edge_separators():
    assert solution.slugify("  hello!  ") == "hello"


def test_v2_truncates_at_word_boundary():
    out = solution.slugify("aaaa bbbb cccc dddd eeee ffff gggg")
    assert out == "aaaa-bbbb-cccc-dddd-eeee-ffff"


def test_v2_never_ends_with_hyphen():
    out = solution.slugify("aaaaaaaaa bbbbbbbbb ccccccccc dddddddd")
    assert len(out) <= 30 and not out.endswith("-")
    assert out == "aaaaaaaaa-bbbbbbbbb-ccccccccc"


def test_v2_short_slug_unchanged():
    assert solution.slugify("hello world") == "hello-world"


def test_v2_single_long_word_hard_cut():
    assert solution.slugify("a" * 40) == "a" * 30
