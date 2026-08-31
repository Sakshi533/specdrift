Update: two small hardening asks from ops. Strip surrounding whitespace off
the input before doing anything else. And a relative path with nothing left
after normalization — the empty string, ".", "./.", etc. — must return "."
instead of an empty string.
