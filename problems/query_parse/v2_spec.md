Update: real query strings are URL-encoded. After splitting on `&` and `=`
(splitting FIRST, so encoded separators never split anything), decode each
key and each value: `%XX` becomes the character with hex code `XX` — accept
uppercase or lowercase hex digits — and `+` becomes a space. You may assume
every `%` starts a well-formed two-hex-digit escape. Overwriting duplicates,
first-`=` splitting, and the empty-string special case are unchanged (note
duplicates are judged on the DECODED key).
