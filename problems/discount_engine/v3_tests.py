import solution


def test_v1_percent_discount_floors():
    assert solution.price(999, [("percent", 10)]) == 900


def test_v1_flat_clamps_at_zero():
    assert solution.price(500, [("flat", 700)]) == 0


def test_v1_no_rules_returns_base():
    assert solution.price(1234, []) == 1234


def test_v2_cap_restores_over_capped_discount():
    assert solution.price(10000, [("percent", 50), ("cap", 2000)]) == 8000


def test_v2_cap_inactive_when_discount_within_cap():
    assert solution.price(10000, [("flat", 1000), ("cap", 2000)]) == 9000


def test_v2_rules_continue_after_cap():
    assert solution.price(10000, [("percent", 50), ("cap", 2000), ("flat", 500)]) == 7500


def test_v2_cap_only_limits_discount_so_far():
    assert solution.price(1000, [("cap", 100), ("percent", 10)]) == 900


def test_v3_percent_applies_to_base():
    assert solution.price(10000, [("percent", 10), ("percent", 10)]) == 8000


def test_v3_percent_after_flat_still_uses_base():
    assert solution.price(1000, [("flat", 500), ("percent", 50)]) == 0


def test_v3_percent_clamps_at_zero():
    assert solution.price(1000, [("flat", 900), ("percent", 50)]) == 0
