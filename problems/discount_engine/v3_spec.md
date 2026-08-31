Update: legal says percent discounts must be computed off the ORIGINAL base
price, not the running price — customers were being shown "20% off" that
worked out to less. So `("percent", p)` now subtracts `p` percent OF BASE
(discount still rounded down to a whole cent) from the running price, clamping
at 0 if it would go negative. Flat rules and caps are unchanged, and rules
still apply strictly in order.
