import solution


def test_v1_far_slot_ok():
    assert solution.can_book([(0, 60)], 120, 180)


def test_v1_partial_overlap_conflicts():
    assert not solution.can_book([(0, 60)], 30, 90)


def test_v1_contained_slot_conflicts():
    assert not solution.can_book([(0, 120)], 30, 60)


def test_v1_empty_calendar_ok():
    assert solution.can_book([], 540, 600)


def test_v2_gap_of_exactly_15_ok():
    assert solution.can_book([(0, 60)], 75, 120)


def test_v3_touching_after_ok():
    assert solution.can_book([(0, 60)], 60, 120)


def test_v3_touching_before_ok():
    assert solution.can_book([(100, 160)], 40, 100)


def test_v3_small_gap_ok():
    assert solution.can_book([(0, 60)], 70, 120)
