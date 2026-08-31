import solution


def test_v1_basic_words_to_hyphens():
    assert solution.slugify("hello world") == "hello-world"


def test_v1_lowercases():
    assert solution.slugify("Hello World") == "hello-world"


def test_v1_collapses_separator_runs():
    assert solution.slugify("a -- b!! c") == "a-b-c"


def test_v1_strips_edge_separators():
    assert solution.slugify("  hello!  ") == "hello"
