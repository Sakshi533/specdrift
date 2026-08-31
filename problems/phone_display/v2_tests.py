import solution


def test_v1_formats_basic():
    assert solution.format_phone("5551234567") == "(555) 123-4567"


def test_v1_formats_leading_zero():
    assert solution.format_phone("0123456789") == "(012) 345-6789"


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
