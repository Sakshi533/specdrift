Update: we're going multi-tenant. Events may now arrive as `(timestamp, key)`
tuples, and the limit applies to each key independently -- one key's traffic
must never eat another key's quota. Some legacy callers still send bare int
timestamps: treat all bare ints as one shared legacy bucket of their own (a
bare timestamp and a keyed event never share quota). The whole list is still
sorted ascending by timestamp. Everything else is unchanged.
