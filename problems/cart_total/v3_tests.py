import solution


def test_v1_sums_price_times_qty():
    items = [
        {"name": "pen", "unit_price": 150, "qty": 2},
        {"name": "pad", "unit_price": 500, "qty": 1},
    ]
    assert solution.cart_total(items) == 800


def test_v1_empty_cart_is_zero():
    assert solution.cart_total([]) == 0


def test_v2_small_qty_lines_never_discounted():
    items = [
        {"name": "pen", "unit_price": 100, "qty": 9},
        {"name": "pad", "unit_price": 500, "qty": 1},
    ]
    assert solution.cart_total(items) == 1400


def test_v3_only_largest_qualifying_line_discounted():
    items = [
        {"name": "clip", "unit_price": 33, "qty": 10},   # 330
        {"name": "cord", "unit_price": 40, "qty": 10},   # 400 -> discounted to 360
    ]
    assert solution.cart_total(items) == 330 + 360


def test_v3_tie_discounts_first_listed_line():
    items = [
        {"name": "tape", "unit_price": 20, "qty": 10},   # 200 -> discounted to 180
        {"name": "glue", "unit_price": 10, "qty": 20},   # 200 full price
    ]
    assert solution.cart_total(items) == 180 + 200


def test_v3_single_qualifying_line_still_discounted():
    items = [{"name": "tack", "unit_price": 7, "qty": 11}]
    assert solution.cart_total(items) == 69  # floor(77 * 0.9)
