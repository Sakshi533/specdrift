def run(ops):
    stack = []
    undo_log = []   # units: lists of (op, value) primitives
    redo_log = []
    txn = None

    def apply(unit):
        for op, v in unit:
            if op == "push":
                stack.append(v)
            else:
                stack.pop()

    def revert(unit):
        for op, v in reversed(unit):
            if op == "push":
                stack.pop()
            else:
                stack.append(v)

    for op in ops:
        if op == "begin":
            txn = []
        elif op == "commit":
            if txn:
                undo_log.append(txn)
            txn = None
        elif op == "undo":
            if not undo_log:
                raise ValueError("nothing to undo")
            unit = undo_log.pop()
            revert(unit)
            redo_log.append(unit)
        elif op == "redo":
            if not redo_log:
                raise ValueError("nothing to redo")
            unit = redo_log.pop()
            apply(unit)
            undo_log.append(unit)
        else:
            if op == "pop":
                prim = ("pop", stack[-1])
            else:
                prim = ("push", int(op.split(":", 1)[1]))
            apply([prim])
            redo_log.clear()
            if txn is not None:
                txn.append(prim)
            else:
                undo_log.append([prim])
    if txn:
        undo_log.append(txn)
    return stack
