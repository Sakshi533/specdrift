Update: people paste numbers with the US country code. After stripping
separators, an 11-digit number whose FIRST digit is 1 is now also valid:
drop the leading 1 and format the remaining 10 digits as usual. An 11-digit
number that does not start with 1 is still invalid (`None`), and a 10-digit
number that happens to start with 1 is left untouched. Output format is
unchanged.
