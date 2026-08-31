Write a Python function `run(ops)`.

`ops` is a list of strings driving a stack of ints (initially empty):

- `"push:N"` -- push the int N (may be negative).
- `"pop"` -- pop the top value. Inputs never pop an empty stack.
- `"undo"` -- revert the most recent mutating op (push or pop) that has not
  already been undone. Undoing a pop restores the popped value.
- `"redo"` -- re-apply the most recently undone op that has not been redone.

push and pop are the mutating ops. Performing a NEW mutating op clears the
redo history. `undo` with nothing left to undo is a no-op; likewise `redo`
with nothing to redo. Return the final stack as a list, bottom first.
