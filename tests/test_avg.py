from src.utils import calc_avg


def test_avg_basic():
    assert calc_avg([1, 2, 3, 4]) == 2.5


def test_avg_ignore_zero():
    assert calc_avg([0, 5, 10], ignore_zero=True) == 7.5


def test_avg_empty():
    try:
        calc_avg([])
    except ZeroDivisionError:
        assert True
    else:
        assert False
