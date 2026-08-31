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


def test_v1_duplicate_key_last_wins():
    assert solution.parse("[s]\nk = 1\nk = 2\n") == {"s": {"k": "2"}}
