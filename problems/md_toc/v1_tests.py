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


def test_v1_underlined_text_is_not_a_header():
    text = "Intro\n----\n# H\n"
    assert _lt(solution.toc(text)) == [(1, "H")]
