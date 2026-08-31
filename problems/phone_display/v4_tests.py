import solution


def test_v2_hyphens_stripped():
    out = solution.format_phone("555-123-4567")
    assert out is not None and out == solution.format_phone("5551234567")


def test_v2_dots_parens_spaces_stripped():
    out = solution.format_phone("(555) 123.4567")
    assert out is not None and out == solution.format_phone("5551234567")


def test_v2_too_few_digits_none():
    assert solution.format_phone("555-1234") is None


def test_v2_too_many_digits_none():
    assert solution.format_phone("5551234567891") is None


def test_v2_letters_none():
    assert solution.format_phone("555-CALL-NOW") is None


def test_v3_leading_one_stripped_from_11_digits():
    out = solution.format_phone("15551234567")
    assert out is not None and out == solution.format_phone("5551234567")


def test_v3_country_code_with_separators():
    out = solution.format_phone("1-555-123-4567")
    assert out is not None and out == solution.format_phone("5551234567")


def test_v3_eleven_digits_not_starting_one_none():
    assert solution.format_phone("25551234567") is None


def test_v3_ten_digits_starting_one_untouched():
    assert solution.format_phone("1234567890") is not None


def test_v4_dash_format_basic():
    assert solution.format_phone("5551234567") == "555-123-4567"


def test_v4_dash_format_leading_zero():
    assert solution.format_phone("0123456789") == "012-345-6789"


def test_v4_dash_format_after_cleaning():
    assert solution.format_phone("(555) 123.4567") == "555-123-4567"


def test_v4_dash_format_after_country_code():
    assert solution.format_phone("15551234567") == "555-123-4567"
