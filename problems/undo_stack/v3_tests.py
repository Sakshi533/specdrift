import solution


def test_v1_push_pop_basic():
    assert solution.run(["push:1", "push:2", "pop"]) == [1]


def test_v1_undo_reverts_push():
    assert solution.run(["push:1", "push:2", "undo"]) == [1]


def test_v1_undo_pop_restores_value():
    assert solution.run(["push:7", "pop", "undo"]) == [7]


def test_v1_redo_reapplies_most_recently_undone():
    # two undos, then one redo: the redo brings back push:1, not push:2
    assert solution.run(["push:1", "push:2", "undo", "undo", "redo"]) == [1]


def test_v2_undo_reverts_whole_transaction():
    ops = ["push:1", "begin", "push:2", "push:3", "commit", "undo"]
    assert solution.run(ops) == [1]


def test_v2_redo_reapplies_whole_transaction():
    ops = ["begin", "push:1", "push:2", "commit", "undo", "redo"]
    assert solution.run(ops) == [1, 2]


def test_v2_transaction_with_pop_reverts_cleanly():
    ops = ["push:1", "push:2", "begin", "pop", "push:9", "commit", "undo"]
    assert solution.run(ops) == [1, 2]


def test_v2_open_transaction_committed_at_end():
    assert solution.run(["push:9", "begin", "push:4", "push:5"]) == [9, 4, 5]


def test_v2_units_undo_in_order():
    # undo #1 removes push:3, undo #2 removes the whole transaction
    ops = ["push:1", "begin", "push:2", "commit", "push:3", "undo", "undo"]
    assert solution.run(ops) == [1]


def test_v2_empty_transaction_not_recorded():
    # begin+commit records nothing, so undo reverts push:1
    assert solution.run(["push:1", "begin", "commit", "undo"]) == []


def test_v3_vacuous_undo_raises():
    try:
        solution.run(["undo"])
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"


def test_v3_vacuous_redo_raises():
    try:
        solution.run(["push:1", "redo"])
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"


def test_v3_redo_after_cleared_history_raises():
    # push:2 wipes the redo history, so the trailing redo must raise
    try:
        solution.run(["push:1", "undo", "push:2", "redo"])
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"


def test_v3_exhausted_undo_raises():
    try:
        solution.run(["push:1", "undo", "undo"])
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"


def test_v3_valid_undo_redo_still_works():
    assert solution.run(["push:1", "push:2", "undo", "redo"]) == [1, 2]
