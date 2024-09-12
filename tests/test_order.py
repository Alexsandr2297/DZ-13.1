import pytest

from src.order import Order


@pytest.fixture()
def order():
    return Order('Зомби в доме', 10, 1999.99)


def test_init(order):
    assert order.purchased_product == "Зомби в доме"
    assert order.quantity_purchased_product == 10
    assert order.total_cost == 1999.99


def test_repr(order):
    assert repr(order) == (
        "Order: купленный товар: Зомби в доме, количество купленного товара 10, итоговая стоимость 1999.99")


def test_total(order):
    assert order.total() == 1999.99 * 10
