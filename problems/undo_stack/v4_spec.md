Update: the UI wants telemetry. `run` must now return a dict instead of the
bare list: `{"stack": <the same final list as before>, "undone": <total
undos performed over the run>, "redone": <total redos performed>}`. An
undone transaction counts as ONE undo (same for redo). Behavior is otherwise
unchanged, including the ValueError on a vacuous undo/redo.
