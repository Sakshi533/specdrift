import solution


def test_v1_sums_price_times_qty():
    items = [
        {"name": "pen", "unit_price": 150, "qty": 2},
        {"name": "pad", "unit_price": 500, "qty": 1},
    ]
    assert solution.cart_total(items) == 800


def test_v1_empty_cart_is_zero():
    assert solution.cart_total([]) == 0


def test_v2_bulk_line_gets_ten_percent_off():
    items = [{"name": "clip", "unit_price": 33, "qty": 10}]
    assert solution.cart_total(items) == 297  # 330 - 10%


def test_v2_discount_rounds_down_per_line():
    items = [{"name": "tack", "unit_price": 7, "qty": 11}]
    assert solution.cart_total(items) == 69  # floor(77 * 0.9) = 69


def test_v2_small_qty_line_not_discounted():
    items = [{"name": "pen", "unit_price": 100, "qty": 9}]
    assert solution.cart_total(items) == 900
