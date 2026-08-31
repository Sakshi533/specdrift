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
        {"name": "clip", "unit_price": 33, "qty": 10},
        {"name": "cord", "unit_price": 40, "qty": 10},
    ]
    assert solution.cart_total(items) == 330 + 360


def test_v3_tie_discounts_first_listed_line():
    items = [
        {"name": "tape", "unit_price": 20, "qty": 10},
        {"name": "glue", "unit_price": 10, "qty": 20},
    ]
    assert solution.cart_total(items) == 180 + 200


def test_v4_coupon_applied_after_bulk_discount():
    items = [
        {"name": "clip", "unit_price": 33, "qty": 10},   # 330 -> 297 (only qualifying)
        {"name": "pad", "unit_price": 50, "qty": 2},     # 100
    ]
    assert solution.cart_total(items, coupon=10) == 357  # floor(397 * 0.9)


def test_v4_coupon_rounds_down():
    items = [{"name": "pen", "unit_price": 333, "qty": 1}]
    assert solution.cart_total(items, coupon=1) == 329  # floor(333 * 0.99) = 329


def test_v4_invalid_coupon_raises():
    ok = 0
    for bad in (-5, 101):
        try:
            solution.cart_total([], coupon=bad)
        except ValueError:
            ok += 1
    assert ok == 2
