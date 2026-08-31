Update: hardening for production. If `text` is empty or contains only
whitespace, return `[]`. If `width` is less than 1, raise `ValueError`.
Everything else unchanged.
