Update: accounting wants fees broken out. Return a tuple
`(final_balance, total_fees)` instead of just the balance — `total_fees` is
the sum of all overdraft fees charged during the run (0 if none). The ledger
behavior itself is unchanged.
