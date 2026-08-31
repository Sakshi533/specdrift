Update: add coupon support. The signature becomes
`cart_total(items, coupon=0)` where `coupon` is an int percentage 0-100.
Apply the coupon to the total AFTER the bulk-discount logic, rounding down to
a whole cent. A `coupon` outside 0-100 must raise `ValueError`. Existing
callers that pass no coupon must keep getting the previous behavior.
