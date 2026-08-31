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


def test_v3_any_order():
    assert solution.secs("30m 1h 30m") == 7200


def test_v3_repeats_accumulate():
    assert solution.secs("10s 10s 10s") == 30


def test_v3_fully_reversed_order():
    assert solution.secs("5s 4m 3h 2d") == 183845


def test_v3_repeated_days():
    assert solution.secs("1d 1d") == 172800


def _raises_value_error(text):
    try:
        solution.secs(text)
    except ValueError:
        return True
    return False


def test_v4_unknown_unit_raises():
    assert _raises_value_error("5x")


def test_v4_bare_number_or_unit_raises():
    assert _raises_value_error("12")
    assert _raises_value_error("h")


def test_v4_empty_and_whitespace_only_raise():
    assert _raises_value_error("")
    assert _raises_value_error("   ")


def test_v4_negative_value_raises():
    assert _raises_value_error("-5m")


def test_v4_zero_is_valid():
    assert solution.secs("0s") == 0
