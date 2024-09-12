import pytest

from src.product import Product


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


def test_product_str_(product_title):
    result = "Зомби в доме, 1999.99 руб. Остаток: 10 шт."
    assert str(product_title) == result


def test_product_add(product_title):
    # Создаем два объекта
    product1 = Product('Зомби в доме', 'Для веселого времяпровождения в компании', 1999.99, 10)
    product2 = Product('Имаджинариум', 'Для веселого времяпровождения в компании', 2999.99, 5)

    expected_sum = 1999.99 * 10 + 2999.99 * 5

    assert (product1 + product2) == expected_sum
    with pytest.raises(TypeError):
        product1 + "Некорректный объект"


def test_display_info(product_title, capsys):
    product_title.display_info()
    captured = capsys.readouterr()
    assert captured.out == 'Product: Зомби в доме, 1999.99, 10\n'
