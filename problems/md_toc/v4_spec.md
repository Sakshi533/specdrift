Update: a flat list doesn't cut it for the sidebar — return a TREE instead.
Each entry becomes a dict `{"title": ..., "slug": ..., "level": ...,
"children": [...]}`. A header nests as a child of the nearest previous
header with a smaller level; a header with no such previous header is a
top-level node, and `toc` returns the list of top-level nodes in document
order. All extraction rules — ATX, setext underlines, fences, trailing
hashes, slugs and slug deduplication — stay exactly as they are.
