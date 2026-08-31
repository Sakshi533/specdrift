import solution


def _lt(entries):
    # project (level, title) from each entry
    return [(e[0], e[1]) for e in entries]


def test_v1_atx_levels():
    text = "# Top\n\nbody\n## Sec\n###### Deep\n"
    assert _lt(solution.toc(text)) == [(1, "Top"), (2, "Sec"), (6, "Deep")]


def test_v1_trailing_hashes_removed():
    text = "## Title ##\n# C#\n"
    assert _lt(solution.toc(text)) == [(2, "Title"), (1, "C#")]


def test_v1_fenced_code_ignored():
    text = "```\n# not a header\n```\n# real\n"
    assert _lt(solution.toc(text)) == [(1, "real")]


def test_v1_non_header_lines_ignored():
    text = "#nospace\n####### seven\n  # indented\n"
    assert solution.toc(text) == []


def test_v2_basic_slug():
    assert solution.toc("# Hello World\n") == [(1, "Hello World", "hello-world")]


def test_v2_nonalnum_runs_become_one_hyphen():
    assert solution.toc("## C++ & Rust!\n") == [(2, "C++ & Rust!", "c-rust")]


def test_v2_edge_hyphens_stripped():
    assert solution.toc("# ...Wow...\n") == [(1, "...Wow...", "wow")]


def test_v2_duplicate_slugs_suffixed_in_order():
    out = solution.toc("# Setup\n## Setup\n### Setup\n")
    assert out == [
        (1, "Setup", "setup"),
        (2, "Setup", "setup-2"),
        (3, "Setup", "setup-3"),
    ]


def test_v2_distinct_titles_can_still_collide():
    out = solution.toc("# A B\n## A-B\n")
    assert out == [(1, "A B", "a-b"), (2, "A-B", "a-b-2")]


def test_v3_setext_h1():
    assert solution.toc("Overview\n====\n") == [(1, "Overview", "overview")]


def test_v3_setext_h2_replaces_old_rule():
    text = "Intro\n----\n# H\n"
    assert solution.toc(text) == [(2, "Intro", "intro"), (1, "H", "h")]


def test_v3_underline_must_be_pure_and_long_enough():
    assert solution.toc("A\n--- x\nB\n--\n") == []


def test_v3_setext_ignored_inside_fence():
    assert solution.toc("```\nX\n===\n```\n") == []


def test_v3_setext_between_atx():
    text = "# A\nMid Point\n---\n## C\n"
    assert solution.toc(text) == [
        (1, "A", "a"),
        (2, "Mid Point", "mid-point"),
        (2, "C", "c"),
    ]
