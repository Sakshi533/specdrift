Update: it also needs to be robust for callers with missing data — either
argument may be an empty list or `None` (treat `None` exactly like an empty
list). It must never raise for those inputs.
