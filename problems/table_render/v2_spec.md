Update: numbers look wrong left-aligned. A cell that LOOKS LIKE AN INTEGER —
an optional leading `-` followed by one or more ASCII digits, and nothing
else — is now RIGHT-aligned within its column (padded on the left instead of
the right). Everything else (`"1.5"`, `"-"`, `"1e3"`, `""`, `"007x"`) stays
left-aligned; `"007"` does look like an integer. Column widths, the `" | "`
separator, trailing-whitespace stripping, and ragged padding are unchanged.
