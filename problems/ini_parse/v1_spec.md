Write a Python function `parse(text)` that parses INI-style text into a dict
of dicts: `{section_name: {key: value}}` (all strings).

Rules:

- A line whose stripped form is `[name]` starts a section. The section name
  is the text between the brackets, stripped. A header always creates its
  section, even if no key lines follow (empty dict).
- A line containing `=` assigns a key in the current section: split on the
  FIRST `=`, strip whitespace around both the key and the value. An empty
  value (`key =`) is stored as `""`.
- Key lines appearing before any section header go in a section named `""`
  (that section exists only if such lines exist).
- Blank (empty or whitespace-only) lines are ignored. Any other line — no
  `=`, not a header — is ignored as well.
- If the same key appears more than once within a section, the LAST value
  wins.
