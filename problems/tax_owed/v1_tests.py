import solution


def test_v1_zero_income_zero_tax():
    assert solution.tax(0) == 0


def test_v1_no_tax_up_to_first_bracket():
    assert solution.tax(100000) == 0


def test_v1_ten_percent_band():
    assert solution.tax(300000) == 20000  # 10% of 200000


def test_v1_twenty_percent_band():
    assert solution.tax(600000) == 60000  # 40000 + 20% of 100000


def test_v1_second_bracket_boundary():
    assert solution.tax(500000) == 40000  # full 10% band, nothing at 20%
