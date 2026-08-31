Update from support: we had the order backwards. The 500-cent restocking fee
comes off FIRST, straight from the tier refund (clamped at zero), and THEN
the opened halving applies, floored — an opened refund is
`max(0, tier_refund - 500) // 2`. Unopened items stay fee-free and unchanged.
