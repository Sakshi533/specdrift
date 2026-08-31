Update from the client: "empty things keep sneaking into the parsed output
— clean them up." We asked which empty things and pinned it down: skip any
pair whose DECODED key is the empty string (so `"a=1&&b=2"` and `"=5"`
contribute nothing), but keep everything else — a key that decodes to
whitespace is NOT empty (`"%20=x"` keeps its one-space key), and empty
VALUES are kept (`"a="` still yields `{"a": [""]}`). `parse("")` is still
`{}`.
