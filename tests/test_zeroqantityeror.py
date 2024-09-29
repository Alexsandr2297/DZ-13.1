from src.order import Order
from src.zeroqantityerror import add_product


def test_add_product_valid_quantity():
    o = Order('Зомби в доме', 10, 19999.99, 1999.99, 10)
    add_product(o)
    assert o.quantity == 10  # проверяем, что количество товара было обновлено


def test_add_product_zero_quantity(capsys):
    o = Order('Зомби в доме', 10, 19999.99, 1999.99, 0)
    add_product(o)
    captured = capsys.readouterr()
    assert captured.out.strip() == ("Товар с нулевым количеством не может быть добавлен\nобработка добавления "
                                    "товара завершена")
