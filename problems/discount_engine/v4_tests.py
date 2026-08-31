import solution


def test_v4_returns_breakdown_dict():
    out = solution.price(1000, [("flat", 100)])
    assert isinstance(out, dict)
    assert set(out) == {"final", "total_discount", "steps"}


def test_v4_final_keeps_percent_of_base_semantics():
    out = solution.price(10000, [("percent", 10), ("percent", 10)])
    assert out["final"] == 8000


def test_v4_total_discount_is_base_minus_final():
    out = solution.price(10000, [("percent", 10), ("percent", 10)])
    assert out["total_discount"] == 2000


def test_v4_steps_track_price_after_each_rule():
    out = solution.price(10000, [("percent", 50), ("cap", 2000), ("flat", 500)])
    assert out["steps"] == [5000, 8000, 7500]
    assert out["final"] == 7500 and out["total_discount"] == 2500


def test_v4_no_rules():
    assert solution.price(1234, []) == {"final": 1234, "total_discount": 0, "steps": []}


def test_v4_flat_clamp_repinned():
    out = solution.price(500, [("flat", 700)])
    assert out["final"] == 0 and out["total_discount"] == 500 and out["steps"] == [0]
