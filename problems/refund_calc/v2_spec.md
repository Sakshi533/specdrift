Update from support: opened items now also pay a flat 500-cent restocking
fee. The fee comes off AFTER the opened halving, and the refund is clamped at
zero — an opened refund is `max(0, tier_refund // 2 - 500)`. Unopened items
are unaffected and never pay the fee.
