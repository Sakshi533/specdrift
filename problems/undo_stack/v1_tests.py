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


def test_v1_new_mutating_op_clears_redo():
    # push:2 wipes the redo history, so the trailing redo is a no-op
    assert solution.run(["push:1", "undo", "push:2", "redo"]) == [2]


def test_v1_undo_with_nothing_is_noop():
    assert solution.run(["undo", "push:1"]) == [1]
