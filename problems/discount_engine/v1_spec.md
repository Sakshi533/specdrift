Write a Python function `price(base, rules)`.

`base` is a price in cents (int >= 0). `rules` is an ordered list of discount
rules applied SEQUENTIALLY, each a tuple:

- `("percent", p)`: compute `p` percent of the current running price, rounding
  the discount amount DOWN to a whole cent, and subtract it.
- `("flat", f)`: subtract `f` cents; the price never goes below 0 (clamp).

Return the final price as an int. No rules means the base price unchanged.
