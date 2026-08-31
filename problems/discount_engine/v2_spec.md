Update: marketing wants stackable promos without giving the store away. Add a
third rule kind `("cap", c)`: when this rule is reached, if the TOTAL discount
granted so far exceeds `c` cents, restore the price to `base - c`. If the
total discount is within the cap, it does nothing. Later rules keep applying
from whatever price the cap left.
