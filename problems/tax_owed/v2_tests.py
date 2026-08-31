import solution


def test_v1_zero_income_zero_tax():
    assert solution.tax(0) == 0


def test_v1_no_tax_up_to_first_bracket():
    assert solution.tax(100000) == 0


def test_v2_deduction_applies_before_brackets():
    assert solution.tax(300000) == 15000  # taxable 250000 -> 10% of 150000


def test_v2_deduction_in_top_bracket():
    assert solution.tax(700000) == 70000  # taxable 650000 -> 40000 + 30000


def test_v2_deduction_down_to_threshold():
    assert solution.tax(150000) == 0  # taxable exactly 100000


def test_v2_deducted_income_floors_at_zero():
    assert solution.tax(30000) == 0  # 30000 - 50000 floors at 0
