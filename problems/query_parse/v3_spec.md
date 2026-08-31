Update: overwriting duplicates loses data the client needs — multi-select
form fields send `"tag=a&tag=b"`. Reversing that rule: duplicates now
COLLECT. Every key maps to a LIST of its decoded values in query order, and
this includes keys that occur once — they map to a one-element list
(`parse("a=1")` is `{"a": ["1"]}`, never `{"a": "1"}`). Splitting, decoding,
and the `parse("") == {}` special case are unchanged; occurrences of the
same DECODED key collect into one list.
