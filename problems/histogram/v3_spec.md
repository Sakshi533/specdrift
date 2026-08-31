Update from the stats team: we are aligning with the R convention — bin
membership flips to left-open, right-closed. Bin `i` is now
`(edges[i], edges[i+1]]`; `under` now counts values `<= edges[0]` and `over`
now counts values `> edges[-1]`. The `(under, counts, over)` return shape is
unchanged.
