Update: lexicographic tag comparison backfired — `"1.0-rc10"` sorted before
`"1.0-rc2"`. New tag rule, replacing plain string comparison entirely: split
each tag into its maximal runs of consecutive digits and consecutive
non-digits (`"rc10"` -> `rc`, `10`; `"a1b"` -> `a`, `1`, `b`), then compare
the two run lists position by position:

- two digit runs compare NUMERICALLY (`"rc2"` is older than `"rc10"`);
- two non-digit runs compare lexicographically (as before);
- a digit run sorts BEFORE a non-digit run at the same position;
- if every compared position is equal and one run list is a prefix of the
  other, the shorter tag is the older one (`"1.0-rc"` is older than
  `"1.0-rc1"`); identical run lists mean equal versions.

Everything else stands: numeric parts first, pre-release before release.
