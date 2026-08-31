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


def test_v2_top_of_band_gets_plus():
    assert solution.grade(88.0) == "B+"


def test_v2_bottom_of_band_gets_minus():
    assert solution.grade(81.0) == "B-"


def test_v2_low_a_gets_minus():
    assert solution.grade(91.0) == "A-"


def test_v2_no_a_plus():
    assert solution.grade(99.0) == "A"


def test_v2_f_has_no_modifiers():
    assert solution.grade(59.0) == "F"


def test_v3_half_rounds_up_into_next_letter():
    assert solution.grade(89.5) == "A-"  # rounds to 90


def test_v3_half_rounds_up_not_bankers():
    assert solution.grade(86.5) == "B+"  # 87, not round-half-even's 86


def test_v3_below_half_rounds_down():
    assert solution.grade(89.4) == "B+"  # rounds to 89


def test_v3_half_up_across_pass_line():
    assert solution.grade(59.5) == "D-"  # rounds to 60
