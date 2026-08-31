Update: the metrics team wants wait numbers inline. Return a list of
`(name, wait)` tuples in the same execution order, where `wait` is the
number of jobs that ran before that job -- the first job to run has wait 0.
Scheduling rules are unchanged.
