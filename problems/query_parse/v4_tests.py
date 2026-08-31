import solution


def test_v1_empty_query_is_empty_dict():
    assert solution.parse("") == {}


def test_v1_keys_come_from_amp_segments():
    assert sorted(solution.parse("a=1&b=2&c=3")) == ["a", "b", "c"]


def test_v2_stored_key_is_decoded():
    assert list(solution.parse("k%41=1")) == ["kA"]


def test_v3_single_occurrence_is_one_element_list():
    assert solution.parse("a=1&b=2") == {"a": ["1"], "b": ["2"]}


def test_v3_duplicates_collect_in_order():
    assert solution.parse("k=1&k=2&k=1") == {"k": ["1", "2", "1"]}


def test_v3_missing_eq_collects_empty_value():
    assert solution.parse("flag&x=1") == {"flag": [""], "x": ["1"]}


def test_v3_split_at_first_eq_only():
    assert solution.parse("k=a=b") == {"k": ["a=b"]}


def test_v3_decoding_still_applies():
    assert solution.parse("q=a%26b&n=John+Doe") == {"q": ["a&b"], "n": ["John Doe"]}


def test_v3_decoded_duplicate_keys_share_one_list():
    assert solution.parse("k%41=1&kA=2") == {"kA": ["1", "2"]}


def test_v4_empty_segments_are_skipped():
    assert solution.parse("a=1&&b=2") == {"a": ["1"], "b": ["2"]}


def test_v4_empty_key_with_value_is_skipped():
    assert solution.parse("=5&x=1") == {"x": ["1"]}


def test_v4_whitespace_key_is_not_empty():
    assert solution.parse("%20=x") == {" ": ["x"]}


def test_v4_empty_values_are_kept():
    assert solution.parse("a=&b") == {"a": [""], "b": [""]}
