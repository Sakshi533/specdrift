Update: users are complaining that when a burst lands at the exact same
timestamp, some of the burst gets denied -- events at the exact same
timestamp shouldn't starve each other. To pin down exactly what we mean:
same-timestamp events for a key are still evaluated in list order and the
window check treats them normally -- no blanket exemption -- BUT if the FIRST
event at a given (key, timestamp) is allowed, every later event with that
exact same key and timestamp is allowed too and consumes no extra quota. If
the first one at that (key, timestamp) was denied, the rest get no special
treatment (and, as before, each still consumes quota).
