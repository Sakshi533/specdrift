import solution


def test_v4_returns_tax_and_rate_dict():
    assert solution.tax(300000) == {"tax": 15000, "effective_rate": 0.05}


def test_v4_effective_rate_rounded_to_4_decimals():
    assert solution.tax(600000) == {"tax": 50000, "effective_rate": 0.0833}


def test_v4_zero_income_has_zero_rate():
    assert solution.tax(0) == {"tax": 0, "effective_rate": 0.0}


def test_v4_zero_tax_income_has_zero_rate():
    assert solution.tax(100000) == {"tax": 0, "effective_rate": 0.0}


def test_v4_high_income_no_deduction_kept():
    assert solution.tax(900000) == {"tax": 120000, "effective_rate": 0.1333}
