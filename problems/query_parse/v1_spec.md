Write a Python function `parse(qs)` that parses a URL query string like
`"a=1&b=2"` into a dict `{key: value}` where keys and values are strings.

Rules:

- Split `qs` on `&`. EVERY resulting segment produces one key/value pair,
  including empty segments (an empty segment yields key `""`, value `""`).
- A segment with `=` splits at its FIRST `=`: text before is the key, text
  after is the value (so `"k=a=b"` gives key `"k"`, value `"a=b"`). Keys and
  values are taken verbatim — no stripping, no decoding.
- A segment without `=` is a key with value `""`.
- When the same key occurs more than once, the LATER occurrence OVERWRITES
  the earlier one.
- The empty query string is special-cased: `parse("")` returns `{}` (not
  `{"": ""}`).
