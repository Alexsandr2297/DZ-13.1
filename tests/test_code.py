import pytest

from src.main import Category
from src.main import Product


@pytest.fixture()
def category_title():
    products = [Product('Зомби в доме', 'Для веселого времяпровождения в компании', 1999.99, 10),
                Product('Имаджинариум', 'Для веселого времяпровождения в компании', 2999.99, 5),
                Product('Экивоки', 'Для веселого времяпровождения в компании', 3999.99, 3)]
    return Category('Настольные игры', 'Для веселого времяпровождения в компании', products)


def test_init(category_title):
    assert category_title.title == "Настольные игры"
    assert category_title.description == "Для веселого времяпровождения в компании"
    assert len(category_title.products) == 3
    assert Category.total_number_of_categories == 1


@pytest.fixture()
def product_title():
    return Product('Зомби в доме', 'Для веселого времяпровождения в компании', 1999.99, 10)


def test_init2(product_title):
    assert product_title.title == "Зомби в доме"
    assert product_title.description == "Для веселого времяпровождения в компании"
    assert product_title.price == 1999.99
    assert product_title.quantity == 10
