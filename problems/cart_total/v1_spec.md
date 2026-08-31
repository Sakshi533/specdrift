Write a Python function `cart_total(items)`.

`items` is a list of dicts, each with keys `"name"` (str), `"unit_price"`
(int, price in cents) and `"qty"` (int, >= 1). Return the cart total in cents
as an int: the sum of `unit_price * qty` over all items. An empty cart totals 0.
