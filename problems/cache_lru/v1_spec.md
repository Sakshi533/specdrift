Write a Python function `trace(capacity, ops)`.

`capacity` is an int >= 1. `ops` is a list of operations, each either
`("put", key, value)` or `("get", key)`. Run them in order against an LRU
cache and return a list with one entry per `get`, in order: the stored value
on a hit, `None` on a miss. A `get` hit makes its key most-recently-used;
so does every `put` -- both a fresh insert and a value update of an existing
key. When a put of a NEW key pushes the cache over capacity, evict the
least-recently-used key. Keys are strings, values are ints; a `get` miss
never changes the cache.
