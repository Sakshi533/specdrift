Update from the rating committee: dropping zero-sum was a mistake for mixed
pairs — rating points were leaking into the pool. When the two players' K
values differ (exactly one side is provisional), BOTH sides now use the
average K = 48 and zero-sum is restored:

    delta_a = round_half_up(48 * (Sa - Ea))
    result  = (ra + delta_a, rb - delta_a)

Pairs with equal K (both provisional, or neither) are computed exactly as
they are today — each side independently with its own K.
