import solution


def _node(title, slug, level, children=None):
    return {"title": title, "slug": slug, "level": level,
            "children": children if children is not None else []}


def test_v1_non_header_lines_ignored():
    text = "#nospace\n####### seven\n  # indented\n"
    assert solution.toc(text) == []


def test_v3_underline_must_be_pure_and_long_enough():
    assert solution.toc("A\n--- x\nB\n--\n") == []


def test_v3_setext_ignored_inside_fence():
    assert solution.toc("```\nX\n===\n```\n") == []


def test_v4_flat_same_level():
    assert solution.toc("# A\n# B\n") == [_node("A", "a", 1), _node("B", "b", 1)]


def test_v4_nesting_chain():
    out = solution.toc("# A\n## B\n### C\n## D\n")
    assert out == [
        _node("A", "a", 1, [
            _node("B", "b", 2, [_node("C", "c", 3)]),
            _node("D", "d", 2),
        ])
    ]


def test_v4_level_jump_nests_under_nearest_smaller():
    out = solution.toc("# A\n### C\n## B\n")
    assert out == [_node("A", "a", 1, [_node("C", "c", 3), _node("B", "b", 2)])]


def test_v4_leading_deep_header_is_top_level():
    out = solution.toc("## First\n# Big\n## Sub\n")
    assert out == [
        _node("First", "first", 2),
        _node("Big", "big", 1, [_node("Sub", "sub", 2)]),
    ]


def test_v4_repins_trailing_hashes_setext_and_dup_slugs():
    out = solution.toc("# Setup ##\nSetup\n----\n")
    assert out == [
        _node("Setup", "setup", 1, [_node("Setup", "setup-2", 2)])
    ]


def test_v4_fenced_code_still_excluded():
    out = solution.toc("```\n# not a header\n```\n# Real\n")
    assert out == [_node("Real", "real", 1)]
