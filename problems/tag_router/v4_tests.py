import solution


def test_v1_user_with_matching_tag_included():
    subs = {"amy": ["python"], "bob": ["golang"]}
    assert solution.route(["python"], subs) == ["amy"]


def test_v1_result_sorted_alphabetically():
    subs = {"zed": ["news"], "amy": ["news"]}
    assert solution.route(["news"], subs) == ["amy", "zed"]


def test_v1_no_match_gives_empty_list():
    subs = {"amy": ["python"]}
    assert solution.route(["cooking"], subs) == []


def test_v1_user_listed_once_despite_multiple_matches():
    subs = {"amy": ["python", "ml"]}
    assert solution.route(["python", "ml"], subs) == ["amy"]


def test_v2_mute_alone_subscribes_to_nothing():
    subs = {"amy": ["-spam"]}
    assert solution.route(["python"], subs) == []


def test_v2_mute_inert_when_muted_tag_absent():
    subs = {"amy": ["python", "-spam"]}
    assert solution.route(["python"], subs) == ["amy"]


def test_v3_positive_match_beats_mute():
    subs = {"amy": ["python", "-spam"]}
    assert solution.route(["python", "spam"], subs) == ["amy"]


def test_v3_mute_still_excludes_without_positive_match():
    subs = {"amy": ["cooking", "-spam"]}
    assert solution.route(["spam", "news"], subs) == []


def test_v3_multiple_mutes_lose_to_one_match():
    subs = {"amy": ["python", "-spam", "-ads"]}
    assert solution.route(["python", "spam", "ads"], subs) == ["amy"]


def test_v4_case_insensitive_match():
    subs = {"amy": ["python"]}
    assert solution.route(["Python"], subs) == ["amy"]


def test_v4_surrounding_whitespace_ignored():
    subs = {"amy": ["  python "]}
    assert solution.route(["python"], subs) == ["amy"]


def test_v4_blank_tags_never_match():
    subs = {"amy": ["", "   "]}
    assert solution.route(["", "  "], subs) == []
