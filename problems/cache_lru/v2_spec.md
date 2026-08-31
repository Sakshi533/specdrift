Update: our metrics dashboard polls the cache and it's wrecking the eviction
order. Add a third op `("peek", key)`: it appends to the result list exactly
like `get` (value on hit, `None` on miss) but must NOT touch recency -- after
a peek, the eviction order is exactly what it was before. Everything else is
unchanged.
