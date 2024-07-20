import pytest

from src.main import Category
from src.main import Product


@pytest.fixture()
def category_title():
    return Category('Настольные игры', 'Для веселого времяпровождения в компании', 'Зомби в доме, '
                                                                                   'Имаджинариум, Экивоки')


def test_init(category_title):
    assert category_title.title == "Настольные игры"
    assert category_title.description == "Для веселого времяпровождения в компании"
    assert category_title.products == "Зомби в доме, Имаджинариум, Экивоки"
    assert category_title.total_number_of_categories == 0
    assert category_title.total_number_of_unique_products == 0


@pytest.fixture()
def product_title():
    return Product('Настольные игры', 'Для веселого времяпровождения в компании', 1999.99, 10)


def test_init2(product_title):
    assert product_title.title == "Настольные игры"
    assert product_title.description == "Для веселого времяпровождения в компании"
    assert product_title.price == 1999.99
    assert product_title.quantity == 10
