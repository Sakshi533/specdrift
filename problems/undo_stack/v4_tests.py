import solution


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


def test_v4_returns_dict_with_stack():
    out = solution.run(["push:1", "push:2", "pop"])
    assert out == {"stack": [1], "undone": 0, "redone": 0}


def test_v4_counts_undos_and_redos():
    out = solution.run(["push:1", "push:2", "undo", "undo", "redo"])
    assert out == {"stack": [1], "undone": 2, "redone": 1}


def test_v4_transaction_counts_as_one_undo():
    out = solution.run(["begin", "push:1", "push:2", "commit", "undo"])
    assert out == {"stack": [], "undone": 1, "redone": 0}


def test_v4_redo_of_transaction_counts_as_one():
    out = solution.run(["begin", "push:1", "commit", "undo", "redo"])
    assert out == {"stack": [1], "undone": 1, "redone": 1}


def test_v4_undo_pop_still_restores_value():
    out = solution.run(["push:7", "pop", "undo"])
    assert out == {"stack": [7], "undone": 1, "redone": 0}


def test_v4_empty_transaction_still_not_recorded():
    out = solution.run(["push:1", "begin", "commit", "undo"])
    assert out == {"stack": [], "undone": 1, "redone": 0}
