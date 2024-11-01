import pytest

from src.smartphone import Smartphone


@pytest.fixture()
def smartphone():
    return Smartphone(2.50, "8 plus", 128, "gray", "iphone",
                      "Apple iPhone 8 Plus поражает своими техническими характеристиками, "
                      "широким набором функций и красивым внешним видом.", 49.999, 2)


def test_init(smartphone):
    assert smartphone.efficiency == 2.50
    assert smartphone.model == "8 plus"
    assert smartphone.amount_of_internal_memory == 128
    assert smartphone.color == "gray"
    assert smartphone.title == "iphone"
    assert smartphone.description == "Apple iPhone 8 Plus поражает своими техническими характеристиками, " \
                                     "широким набором функций и красивым внешним видом."
    assert smartphone.price == 49.999
    assert smartphone.quantity == 2


def test_display_info(smartphone, capsys):
    smartphone.display_info()
    captured = capsys.readouterr()
    assert captured.out == 'Smartphone: 2.5ГГц, 8 plus, 128ГБ, gray, 49.999 Rub, 2 шт\n'
