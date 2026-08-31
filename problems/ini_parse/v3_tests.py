import solution


def test_v1_basic_sections():
    text = "[db]\nhost = localhost\n\nport=5432\n\n[cache]\n"
    assert solution.parse(text) == {
        "db": {"host": "localhost", "port": "5432"},
        "cache": {},
    }


def test_v1_keys_before_any_section():
    assert solution.parse("root = yes\n[a]\nx = 1\n") == {
        "": {"root": "yes"},
        "a": {"x": "1"},
    }


def test_v1_whitespace_stripped():
    assert solution.parse("[ srv ]\n   timeout   =   30 s  \n") == {
        "srv": {"timeout": "30 s"}
    }


def test_v1_empty_value():
    assert solution.parse("[s]\nkey =\nother=x\n") == {
        "s": {"key": "", "other": "x"}
    }


def test_v2_semicolon_comment_line_ignored():
    text = "[s]\n; disabled = true\nk = 1\n"
    assert solution.parse(text) == {"s": {"k": "1"}}


def test_v2_indented_hash_comment_ignored():
    text = "[s]\n   # port = 9\nport = 6\n"
    assert solution.parse(text) == {"s": {"port": "6"}}


def test_v2_semicolon_inside_value_kept():
    text = "[s]\npath = C:/x;D:/y ; keep me\n"
    assert solution.parse(text) == {"s": {"path": "C:/x;D:/y ; keep me"}}


def test_v2_comment_looking_like_header_ignored():
    text = "[a]\nx = 1\n; [b] = decoy\ny = 2\n"
    assert solution.parse(text) == {"a": {"x": "1", "y": "2"}}


def test_v3_duplicate_key_first_wins():
    assert solution.parse("[s]\nk = 1\nk = 2\n") == {"s": {"k": "1"}}


def test_v3_later_duplicate_does_not_disturb_others():
    text = "[s]\na = 1\nb = 2\na = 9\nc = 3\n"
    assert solution.parse(text) == {"s": {"a": "1", "b": "2", "c": "3"}}


def test_v3_first_wins_in_default_section():
    assert solution.parse("k = old\nk = new\n[a]\nx = 1\n") == {
        "": {"k": "old"},
        "a": {"x": "1"},
    }


def test_v3_comment_does_not_count_as_occurrence():
    text = "[s]\n; k = zero\nk = 1\nk = 2\n"
    assert solution.parse(text) == {"s": {"k": "1"}}
