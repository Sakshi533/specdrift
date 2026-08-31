Write a Python function `refund(price, days, opened)`.

`price` is the purchase price in cents (int), `days` is the number of whole
days since purchase (int), `opened` is a bool. Refund tiers: within 14 days
the refund is the full price; within 30 days it is 50% of the price, floored
(`price // 2`); after that it is 0. If the item was opened, the tier refund
is halved again, floored. Return the refund in cents as an int.
