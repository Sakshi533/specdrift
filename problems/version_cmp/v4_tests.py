import solution


def test_v1_shorter_component_list_can_win():
    assert solution.cmp("1.2.10", "1.3") == -1


def test_v1_missing_components_are_zero():
    assert solution.cmp("1.2", "1.2.0") == 0


def test_v1_numeric_not_lexicographic():
    assert solution.cmp("1.10", "1.9") == 1


def test_v1_leading_zeros_ignored():
    assert solution.cmp("1.02", "1.2") == 0


def test_v1_returns_sign_triple():
    assert solution.cmp("0.9", "1.0") == -1
    assert solution.cmp("1.0", "0.9") == 1
    assert solution.cmp("3", "3.0.0") == 0


def test_v2_prerelease_before_release():
    assert solution.cmp("1.2.0-beta", "1.2.0") == -1


def test_v2_release_after_prerelease():
    assert solution.cmp("1.2.0", "1.2.0-beta") == 1


def test_v2_tags_compare_when_bases_equal():
    assert solution.cmp("1.0-alpha", "1.0-beta") == -1


def test_v2_missing_components_zero_with_tags():
    assert solution.cmp("2.0-rc", "2.0.0-rc") == 0


def test_v2_numeric_part_beats_any_tag():
    assert solution.cmp("1.0.1", "1.0-zzz") == 1


def test_v3_numeric_tag_runs_compare_numerically():
    assert solution.cmp("1.0-rc2", "1.0-rc10") == -1


def test_v3_numeric_run_after_common_alpha_prefix():
    assert solution.cmp("2.1-beta9", "2.1-beta10") == -1


def test_v3_prefix_run_list_sorts_first():
    assert solution.cmp("1.0-rc", "1.0-rc1") == -1


def test_v3_digit_run_before_alpha_run():
    assert solution.cmp("1.0-rc1", "1.0-rcx") == -1


def _raises_value_error(a, b):
    try:
        solution.cmp(a, b)
    except ValueError:
        return True
    return False


def test_v4_empty_string_raises():
    assert _raises_value_error("", "1.0")
    assert _raises_value_error("1.0", "")


def test_v4_non_digit_component_raises():
    assert _raises_value_error("1.x.0", "1.0")


def test_v4_whitespace_in_component_raises():
    assert _raises_value_error("1. 2", "1.1")


def test_v4_empty_prerelease_tag_raises():
    assert _raises_value_error("1.0-", "1.0")
