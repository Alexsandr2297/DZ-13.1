from src.order import Order


class ZeroQuantityError(Exception):
    """Класс для исключения, если товар равен нулю"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def add_product(order):
    """Добавляет товар в заказу, проверяет количество"""
    try:
        if order.quantity == 0:
            raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")
    except ZeroQuantityError as t:
        print(t.message)
    else:
        print(f"Товар успешно добавлен")
    finally:
        print("обработка добавления товара завершена")


o = Order('Зомби в доме', 10, 19999.99, 1999.99, 0)
add_product(o)

# def add_product(category, product):
#     try:
#         if product.quantity == 0:
#             raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")
#         category.products.append(product)
#         print(f"Товар '{product.title}' добавлен в категорию '{category.title}'")
#     except ZeroQuantityError as e:
#         print(e.message)
#     else:
#         print("Товар добавлен успешно")
#     finally:
#         print("Обработка добавления товара завершена")


# category1 = Category('Настольные игры', 'Для веселого времяпровождения в компании',
#                      [Product('Зомби в доме', 'Для веселого времяпровождения в компании', 1999.99, 10),
#                       Product('Имаджинариум', 'Для веселого времяпровождения в компании', 2999.99, 5),
#                       Product('Экивоки', 'Для веселого времяпровождения в компании', 3999.99, 3)],
#                      1999.99, 18)
#
# product1 = Product('Зомби в доме', 'Для веселого времяпровождения в компании', 1999.99, 1)
#
# add_product(category1, product1)
