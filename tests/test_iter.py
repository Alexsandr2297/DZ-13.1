import pytest

from src.category_iterator import CategoryIterator
from src.product import Product


def test_iterator():
    # Пустой список
    products = CategoryIterator([])
    with pytest.raises(StopIteration):
        next(products)

    # Список с одним продуктом
    product1 = Product("Зомби в доме", "Для веселого времяпровождения в компании", 1999.99, 10)
    products = CategoryIterator([product1])
    assert next(products) == product1
    with pytest.raises(StopIteration):
        next(products)

    # Список с несколькими продуктами
    product2 = Product("Имаджинариум", "Для веселого времяпровождения в компании", 2999.99, 5)
    products = CategoryIterator([product1, product2])
    assert next(products) == product1
    assert next(products) == product2
    with pytest.raises(StopIteration):
        next(products)
