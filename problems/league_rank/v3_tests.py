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
    ]  # 3-team tie on 3 pts; gd: Alba +3, Cava 0, Brix -3
    assert solution.table(results) == ["Alba", "Cava", "Brix"]


def test_v1_goals_scored_breaks_gd_ties():
    results = [
        ("Utd", "City", 3, 2),
        ("City", "Rovers", 1, 0),
        ("Rovers", "Utd", 2, 1),
    ]  # 3-team tie on 3 pts, gd 0; gf: Utd 4, City 3, Rovers 2
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


def test_v3_head_to_head_beats_goal_difference():
    results = [
        ("Dux", "Elm", 1, 0),
        ("Elm", "Fir", 5, 0),
    ]  # Dux and Elm both 3 pts; Elm gd +4 vs Dux +1, but Dux won the meeting
    assert solution.table(results) == ["Dux", "Elm", "Fir"]


def test_v3_split_head_to_head_falls_back_to_gd():
    results = [
        ("Mint", "Nook", 2, 0),
        ("Nook", "Mint", 1, 0),
    ]  # both 3 pts, h2h 3-3 -> fall back to gd (Mint +1, Nook -1)
    assert solution.table(results) == ["Mint", "Nook"]


def test_v3_drawn_head_to_head_falls_back_to_gd():
    results = [
        ("Gale", "Hart", 1, 1),
        ("Gale", "Ike", 3, 0),
        ("Hart", "Jots", 1, 0),
    ]  # Gale and Hart both 4 pts, h2h 1-1 -> gd decides (Gale +3, Hart +1)
    assert solution.table(results) == ["Gale", "Hart", "Jots", "Ike"]


def test_v3_three_way_tie_skips_head_to_head():
    results = [
        ("Pyx", "Quill", 1, 0),
        ("Quill", "Rook", 4, 0),
        ("Rook", "Pyx", 2, 1),
    ]  # 3-team tie on 3 pts: gd chain applies (Quill +3, Pyx 0, Rook -3)
    # even though Pyx beat Quill head-to-head
    assert solution.table(results) == ["Quill", "Pyx", "Rook"]
