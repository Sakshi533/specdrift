Update: garbage inputs are reaching this function in production. A negative
`price` or a negative `days` must raise `ValueError`. And QA keeps arguing
about the fences, so pin them: day 14 still counts as "within 14 days" (full
tier) and day 15 does not; day 30 still counts as "within 30 days" (half
tier) and day 31 does not. Nothing else changes.
