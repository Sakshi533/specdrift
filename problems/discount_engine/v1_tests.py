import solution


def test_v1_percent_on_running_price():
    assert solution.price(10000, [("percent", 10), ("percent", 10)]) == 8100


def test_v1_percent_discount_floors():
    assert solution.price(999, [("percent", 10)]) == 900  # discount floor(99.9) = 99


def test_v1_flat_clamps_at_zero():
    assert solution.price(500, [("flat", 700)]) == 0


def test_v1_sequential_order_matters():
    assert solution.price(1000, [("flat", 500), ("percent", 50)]) == 250


def test_v1_no_rules_returns_base():
    assert solution.price(1234, []) == 1234
