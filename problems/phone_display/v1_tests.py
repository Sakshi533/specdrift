import solution


def test_v1_formats_basic():
    assert solution.format_phone("5551234567") == "(555) 123-4567"


def test_v1_formats_leading_zero():
    assert solution.format_phone("0123456789") == "(012) 345-6789"
