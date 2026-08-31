Update: we need anchor links. Every entry gains a slug as a third element —
return `(level, title, slug)`. Slug = the title lowercased, every run of
non-alphanumeric characters replaced by a single hyphen, then leading and
trailing hyphens stripped. When a slug repeats within the document, the
later duplicates get `-2`, `-3`, ... appended in document order (the first
occurrence stays bare).
