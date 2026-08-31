Update: the registrar objects to fractional cutoffs. Scores must now be
rounded to the nearest integer FIRST, and the rounded value fed to the band
table. Exactly .5 always rounds UP (89.5 becomes 90, which is an "A-") —
always up, not Python's round-half-to-even.
