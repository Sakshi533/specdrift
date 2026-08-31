import solution


def test_v1_a_band():
    assert solution.grade(95.0) == "A"


def test_v1_b_band():
    assert solution.grade(85.0) == "B"


def test_v1_c_band():
    assert solution.grade(75.0) == "C"


def test_v1_d_band():
    assert solution.grade(65.0) == "D"


def test_v1_f_below_60():
    assert solution.grade(42.0) == "F"
