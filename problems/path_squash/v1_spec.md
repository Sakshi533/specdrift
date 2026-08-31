Write a Python function `squash(path)`.

`path` is a POSIX-style path string. Normalize it:

- collapse runs of repeated "/" into a single "/",
- remove "." segments,
- the result is absolute (leading "/") iff the input started with "/",
  and relative otherwise,
- no trailing "/" — except the root path, which is exactly "/".

Leave ".." segments exactly where they are; do not resolve them.
