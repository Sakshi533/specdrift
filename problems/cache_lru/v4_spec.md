Update: SRE wants observability, so the return shape changes. `trace` must
now return a dict
`{"results": [...], "evicted": [...], "hits": n, "misses": n}` where
`"results"` is exactly the list you returned before, `"evicted"` lists
evicted keys in eviction order, and `"hits"`/`"misses"` count lookups: every
`get` and every `peek` is a hit if the key is present, a miss otherwise.
Puts count toward neither. All the cache behavior rules stand exactly as
they are.
