Update: the ` (xN)` suffix breaks the downstream column parser — we have to
walk that back. Use a PREFIX instead: put `N x ` in front of the collapsed
line (e.g. `2 x disk full`). Still only for runs of 2 or more; a line that
appears once stays exactly as-is, no prefix.
