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


def test_add_product(category_title):
    assert category_title.products == [
        'Зомби в доме, 1999.99 руб. Остаток:10 шт.',
        'Имаджинариум, 2999.99 руб. Остаток:5 шт.',
        'Экивоки, 3999.99 руб. Остаток:3 шт.'
    ]
    # Добавим новый продукт и проверим, что он добавился правильно
    new_product = Product('Монополия', 'Классическая настольная игра', 1999.99, 12)
    category_title.add_products(new_product)

    assert len(category_title.products) == 4
    assert category_title.products[-1] == 'Монополия, 1999.99 руб. Остаток:12 шт.'


@pytest.fixture()
def product_title():
    return Product('Зомби в доме', 'Для веселого времяпровождения в компании', 1999.99, 10)


def test_init2(product_title):
    assert product_title.title == "Зомби в доме"
    assert product_title.description == "Для веселого времяпровождения в компании"
    assert product_title.price == 1999.99
    assert product_title.quantity == 10


def test_products(product_title):
    assert product_title.title == "Зомби в доме"
    assert product_title.description == "Для веселого времяпровождения в компании"
    assert product_title.price == 1999.99
    assert product_title.quantity == 10
