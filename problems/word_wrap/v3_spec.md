Update: the client hates the mid-word breaks — scrap them. A word longer
than `width` goes back to getting its own line and overflowing, exactly like
before the last change.

New typographic rule though: a line must never END with one of the articles
"a", "an", "the" (lowercase, exact match). When greedy packing would leave an
article at the end of a line, move that article down to start the next line
instead (if the line then still ends with an article, move that one too).
Exception: if the article is the ONLY word on its line, leave it there.
Example: `wrap("she saw a bird", 9)` -> `["she saw", "a bird"]`, not
`["she saw a", "bird"]`.
