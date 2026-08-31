import solution


def test_v1_far_slot_ok():
    assert solution.can_book([(0, 60)], 120, 180)


def test_v1_partial_overlap_conflicts():
    assert not solution.can_book([(0, 60)], 30, 90)


def test_v1_contained_slot_conflicts():
    assert not solution.can_book([(0, 120)], 30, 60)


def test_v1_empty_calendar_ok():
    assert solution.can_book([], 540, 600)
