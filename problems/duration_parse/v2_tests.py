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


def test_v2_days_unit():
    assert solution.secs("1d 2h") == 93600


def test_v2_multi_digit_values():
    assert solution.secs("120m") == 7200


def test_v2_flexible_whitespace():
    assert solution.secs("  3h    20m ") == 12000


def test_v2_full_d_h_m_s_chain():
    assert solution.secs("2d 3h 4m 5s") == 183845
