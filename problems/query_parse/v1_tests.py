import solution


def test_v1_basic_pairs():
    assert solution.parse("a=1&b=2") == {"a": "1", "b": "2"}


def test_v1_later_duplicate_overwrites():
    assert solution.parse("k=1&k=2") == {"k": "2"}


def test_v1_missing_eq_means_empty_value():
    assert solution.parse("flag&x=1") == {"flag": "", "x": "1"}


def test_v1_split_at_first_eq_only():
    assert solution.parse("k=a=b") == {"k": "a=b"}


def test_v1_empty_query_is_empty_dict():
    assert solution.parse("") == {}


def test_v1_keys_come_from_amp_segments():
    assert sorted(solution.parse("a=1&b=2&c=3")) == ["a", "b", "c"]
