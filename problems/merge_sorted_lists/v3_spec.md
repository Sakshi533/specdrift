Update: scratch the deduplication — we DO want duplicates kept after all, but
now each element must be tagged with which input list it came from. Return a
list of `(value, source)` tuples where `source` is `'a'` or `'b'`, sorted
ascending by value; for equal values, all elements from `a` come before those
from `b`. Inputs must still not be mutated.
