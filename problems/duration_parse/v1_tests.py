import solution


def test_v1_full_h_m_s():
    assert solution.secs("2h 30m 15s") == 9015


def test_v1_single_term():
    assert solution.secs("45m") == 2700


def test_v1_subset_keeps_order():
    assert solution.secs("1h 5s") == 3605


def test_v1_returns_int():
    result = solution.secs("59s")
    assert result == 59
    assert isinstance(result, int)
