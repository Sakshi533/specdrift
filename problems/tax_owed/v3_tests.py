import solution


def test_v1_zero_income_zero_tax():
    assert solution.tax(0) == 0


def test_v1_no_tax_up_to_first_bracket():
    assert solution.tax(100000) == 0


def test_v2_deduction_applies_before_brackets():
    assert solution.tax(300000) == 15000


def test_v2_deduction_in_top_bracket():
    assert solution.tax(700000) == 70000


def test_v2_deduction_down_to_threshold():
    assert solution.tax(150000) == 0


def test_v2_deducted_income_floors_at_zero():
    assert solution.tax(30000) == 0


def test_v3_high_income_gets_no_deduction():
    assert solution.tax(900000) == 120000  # brackets on full 900000


def test_v3_deduction_still_applies_at_cutoff():
    assert solution.tax(800000) == 90000  # taxable 750000 -> 40000 + 50000


def test_v3_deduction_lost_just_above_cutoff():
    assert solution.tax(800001) == 100000  # brackets on full 800001
