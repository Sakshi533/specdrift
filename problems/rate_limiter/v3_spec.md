Update: we're walking back the free pass on denied requests -- abuse found
clients hammering us for free while throttled. A denied event now DOES
consume quota: it counts toward the window for every later event of the same
key, exactly like an allowed one. The allow/deny decision rule itself is
unchanged, and the returned list is still one bool per event.
