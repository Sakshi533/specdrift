Update: we're reversing part of the recency rule. Background sync jobs
rewrite values constantly and were keeping stale keys alive forever. A `put`
to a key ALREADY in the cache now updates the value but does NOT refresh
recency -- the key keeps its old position in the eviction order. A put that
inserts a fresh key still enters as most-recently-used (and can still
trigger an eviction). `get` hits still refresh, `peek` still doesn't.
