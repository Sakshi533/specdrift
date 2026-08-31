Write a Python function `toc(text)` that extracts a table of contents from
markdown text. Return a list of `(level, title)` tuples in document order.

- A header line is 1-6 `#` characters at the very start of the line,
  followed by a single space, then the title. No leading indentation
  allowed. A run of 7+ hashes, or hashes with no space after them, is not a
  header.
- The title is everything after the hashes and the space, stripped of
  surrounding whitespace. A trailing run of `#` is removed as well, together
  with the whitespace before it — but only when whitespace separates it from
  the text: `## Title ##` gives `Title`, while `# C#` keeps its `#`.
- Fenced code blocks: a line starting with three backticks toggles fence
  state, and lines inside a fence are never headers.
- Only these `#`-style (ATX) lines are headers — nothing else in the
  document produces an entry.
