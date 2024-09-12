import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawn_grass import Product


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
    assert Category.total_number_of_unique_products == 3


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
    with pytest.raises(TypeError):
        category_title.add_products("Некорректный продукт")


def test__category_str__(category_title):
    product_count = Category("Настольные игры", "Для веселого времяпровождения в компании",
                             [Product('Зомби в доме', 'Для веселого времяпровождения в компании', 1999.99, 10),
                              Product('Имаджинариум', 'Для веселого времяпровождения в компании', 2999.99, 5),
                              Product('Экивоки', 'Для веселого времяпровождения в компании', 3999.99, 3)])
    result = "Настольные игры, количество продуктов: 3 шт."
    assert str(product_count) == result


def test_iter():
    products = [
        Product("Зомби в доме", "Для веселого времяпровождения в компании", 1999.99, 10),
        Product("Имаджинариум", "Для веселого времяпровождения в компании", 2999.99, 5),
        Product('Экивоки', 'Для веселого времяпровождения в компании', 3999.99, 3)
    ]
    category_iterator = CategoryIterator(products)
    assert next(category_iterator).title == "Зомби в доме"
    assert next(category_iterator).title == "Имаджинариум"
    assert next(category_iterator).title == "Экивоки"

    with pytest.raises(StopIteration):
        next(category_iterator)


def test_category_total(category_title):
    assert category_title.total() == 1999.99 * 10 + 2999.99 * 5 + 3999.99 * 3


def test_repr(category_title):
    assert repr(category_title) == ("Category, Настольные игры, Для веселого времяпровождения в компании, ['Зомби "
                                    "в доме, 1999.99 руб. Остаток:10 шт.', 'Имаджинариум, 2999.99 руб. Остаток:5 "
                                    "шт.', 'Экивоки, 3999.99 руб. Остаток:3 шт.']")
