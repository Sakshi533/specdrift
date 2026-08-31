def run(ops):
    stack = []
    undo_log = []
    redo_log = []

    def apply(prim):
        op, v = prim
        if op == "push":
            stack.append(v)
        else:
            stack.pop()

    def revert(prim):
        op, v = prim
        if op == "push":
            stack.pop()
        else:
            stack.append(v)

    for op in ops:
        if op == "undo":
            if undo_log:
                prim = undo_log.pop()
                revert(prim)
                redo_log.append(prim)
        elif op == "redo":
            if redo_log:
                prim = redo_log.pop()
                apply(prim)
                undo_log.append(prim)
        else:
            if op == "pop":
                prim = ("pop", stack[-1])
            else:
                prim = ("push", int(op.split(":", 1)[1]))
            apply(prim)
            undo_log.append(prim)
            redo_log.clear()
    return stack
