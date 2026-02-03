from src.utils import unique_sorted, char_counter


def test_unique_sorted():
    assert unique_sorted([5, 2, 2, 7, 5]) == [2, 5, 7]


def test_char_counter():
    txt = "Hello, World!"
    result = char_counter(txt)
    # без учета регистра, без пробелов и пунктуации
    assert result == {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}
