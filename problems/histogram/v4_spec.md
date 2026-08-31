Update from the client: repeated identical edges keep confusing people — the
app does something nobody can predict with them; do something sensible. We
asked what "sensible" should mean exactly and pinned it down: repeated edges
are allowed, and a zero-width bin (`edges[i] == edges[i+1]`) acts as a
catch-bin for exactly its edge value. Precisely: the under/over rules are
unchanged and are applied first; a remaining value equal to some zero-width
bin's edge is counted in the FIRST such bin scanning left to right; every
other remaining value follows the existing `(edges[i], edges[i+1]]` rule, and
a zero-width bin never counts any other value. Strictly increasing edges
behave exactly as they do today.
