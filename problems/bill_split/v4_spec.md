Update from the client: a host added their newborn to the bill with weight 0
as a joke and the app charged the baby a cent — zero-weight people shouldn't
mess things up. We asked what that should mean exactly and pinned it down:
weight 0 is allowed, a zero-weight person always gets exactly 0 cents and is
skipped entirely by the leftover-cent distribution (leftover cents go only to
positive-weight people, in the same smallest-remainder order); a weights list
that is ALL zeros raises `ValueError`.
