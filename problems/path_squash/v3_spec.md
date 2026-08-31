Update from the security team: we got hit by path traversal attacks, so ".."
must NOT be resolved silently anymore. If any segment of the input is exactly
".." — anywhere, absolute or relative — raise `ValueError`. Names that merely
contain dots ("a..", "..b", "...") are ordinary segments and stay legal.
