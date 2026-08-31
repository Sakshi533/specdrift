Update: we need transactions. Two new ops, `"begin"` and `"commit"`: the
mutating ops between them form one transaction that undo/redo treats as a
SINGLE unit -- one undo reverts the whole batch, one redo re-applies it. An
empty transaction (begin then immediately commit) is not recorded, so undo
skips past it. An input that ends with an open transaction treats it as
committed. You will never see nested begins, a commit without a begin, or
undo/redo inside a transaction.
