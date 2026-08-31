import solution


def test_v1_points_order_wins_over_everything():
    results = [
        ("Rex", "Sol", 2, 0),
        ("Rex", "Tam", 3, 0),
        ("Sol", "Tam", 2, 0),
    ]  # Rex 6 pts, Sol 3, Tam 0
    assert solution.table(results) == ["Rex", "Sol", "Tam"]


def test_v1_draw_gives_one_point_each():
    assert solution.table([("Ivy", "Jay", 1, 1)]) == ["Ivy", "Jay"]


def test_v1_goal_difference_breaks_point_ties():
    results = [
        ("Alba", "Brix", 4, 0),
        ("Brix", "Cava", 2, 1),
        ("Cava", "Alba", 2, 1),
    ]  # all 3 pts; gd: Alba +3, Cava 0, Brix -3
    assert solution.table(results) == ["Alba", "Cava", "Brix"]


def test_v1_goals_scored_breaks_gd_ties():
    results = [
        ("Utd", "City", 3, 2),
        ("City", "Rovers", 1, 0),
        ("Rovers", "Utd", 2, 1),
    ]  # all 3 pts, gd 0; gf: Utd 4, City 3, Rovers 2
    assert solution.table(results) == ["Utd", "City", "Rovers"]


def test_v1_name_ascending_is_last_resort():
    results = [
        ("Kite", "Lark", 1, 0),
        ("Lark", "Moth", 1, 0),
        ("Moth", "Kite", 1, 0),
    ]  # perfectly symmetric: 3 pts, gd 0, gf 1 each
    assert solution.table(results) == ["Kite", "Lark", "Moth"]


def test_v2_fewer_games_ranks_higher():
    results = [
        ("Zeal", "Opal", 2, 0),
        ("Zeal", "Pico", 1, 1),
        ("Ant", "Opal", 3, 0),
        ("Ant", "Pico", 0, 0),
        ("Quon", "Ant", 1, 0),
    ]  # Zeal and Ant both 4 pts, gd +2, gf 3; Zeal played 2, Ant played 3
    assert solution.table(results) == ["Zeal", "Ant", "Quon", "Pico", "Opal"]


def test_v2_away_appearances_count_as_games():
    results = [
        ("Ura", "Yolk", 0, 2),
        ("Vex", "Yolk", 1, 1),
        ("Bram", "Ura", 3, 0),
        ("Bram", "Vex", 0, 0),
        ("Wode", "Bram", 1, 0),
    ]  # Yolk and Bram both 4 pts, gd +2, gf 3; Yolk 2 games, Bram 3
    assert solution.table(results) == ["Yolk", "Bram", "Wode", "Vex", "Ura"]


def test_v2_goals_scored_still_beats_games_played():
    results = [
        ("Coral", "Xexa", 3, 0),
        ("Yara", "Coral", 1, 0),
        ("Dune", "Zopa", 2, 0),
    ]  # Coral (gf 3, 2 games) still ranks above Dune (gf 2, 1 game)
    assert solution.table(results) == ["Coral", "Dune", "Yara", "Zopa", "Xexa"]
