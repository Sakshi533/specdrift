import solution


def test_v1_sums_price_times_qty():
    items = [
        {"name": "pen", "unit_price": 150, "qty": 2},
        {"name": "pad", "unit_price": 500, "qty": 1},
    ]
    assert solution.cart_total(items) == 800


def test_v1_empty_cart_is_zero():
    assert solution.cart_total([]) == 0
