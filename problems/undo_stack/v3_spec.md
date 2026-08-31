Update: silent no-ops are confusing users -- they mash undo, nothing happens,
and they file bug reports. Reversing the earlier decision: `undo` with
nothing left to undo must now raise `ValueError`, and likewise `redo` with
nothing left to redo. Everything else stays exactly as is.
