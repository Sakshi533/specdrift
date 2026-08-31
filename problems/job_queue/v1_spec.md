Write a Python function `order(jobs)`.

`jobs` is a list of `(name, priority)` tuples; `priority` is an int, and a
job's submission order is its position in the list. Return the list of names
in execution order: higher priority runs first, and jobs of equal priority
run FIFO (earlier submission first). Names are unique.
