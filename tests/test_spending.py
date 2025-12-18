from src.spending import get_total


def test_get_total():
    costs = {"apple": 1.0, "banana": 2.0}
    items = ["apple", "banana", "orange"]
    tax = 0.1

    assert get_total(costs, items, tax) == 3.3
