Update: three things, all widenings. (1) New unit `d` (days, 86400 s), which
comes before `h` in the unit order — so the order is now `d`, `h`, `m`, `s`,
still each at most once. (2) Values may have any number of digits: `"120m"`,
`"1000s"`. (3) Whitespace is flexible now — any amount of whitespace may
separate terms, and leading/trailing whitespace is allowed.
