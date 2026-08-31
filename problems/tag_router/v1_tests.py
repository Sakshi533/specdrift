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
