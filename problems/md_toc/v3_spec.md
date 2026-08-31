Update: our writers use underlined headers and product wants them in the
TOC — this overturns the old "only `#` lines are headers" rule. A non-empty
line followed by an underline line is now a header: `===...` makes it level
1, `---...` makes it level 2. This applies ONLY when the underline line is
at least 3 characters long and consists solely of that one character
(`--- x` and `--` do not count). The underline line is consumed. Inside
fenced code blocks nothing changes — no headers of any kind there. Titles
are the underlined line stripped; slug rules apply as usual.
