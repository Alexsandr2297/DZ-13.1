from abc import ABC

from src.product import Product


class LawnGrass(Product, ABC):
    """Класс для травы газонной"""
    strange_producer: str  # страна-производитель
    germination_period: int  # срок-прорастания
    color: str  # цвет

    def __init__(self, strange_producer, germination_period, color, title, description, price, quantity):
        """Конструктор для травы газонной"""

        self.strange_producer = strange_producer
        self.germination_period = germination_period
        self.color = color
        super().__init__(title, description, price, quantity)

    def display_info(self):
        """Выводит информацию попродукту"""
        print(
            f"Lawn_grass: {self.title}, {self.price} Rub, {self.quantity} шт, {self.strange_producer}, "
            f"{self.germination_period} Месяц, {self.color}")


law = LawnGrass("Italy", 2, "green", "lawn", "Эта трава - "
                                             "идеальное растение для создания густого и привлекательного газона, "
                                             "легко выделяющегося на фоне других культур.", 9.999, 5)

# Вывожу информацию о категории
#
# product1 = Product('Зомби в доме', 'Для веселого времяпровождения в компании', 1999.99, 10)

# category1 = Category('Настольные игры', 'Для веселого времяпровождения в компании',
#                      [Product('Зомби в доме', 'Для веселого времяпровождения в компании', 1999.99, 10),
#                       Product('Имаджинариум', 'Для веселого времяпровождения в компании', 2999.99, 5),
#                       Product('Экивоки', 'Для веселого времяпровождения в компании', 3999.99, 3)])
# smartphone = Smartphone(2.50, "iphone 8 plus", 128, "grea", "smarthone",
#                         "ok", 1.999, 2)
# lwan = LawnGrass("Italiya", 2, "green", "dsdc", "sdcsc", 2.999, 3)
# category1.add_products(smartphone)
# product2 = Product('Имаджинариум', 'Для веселого времяпровождения в компании', 2999.99, 5)
# print(product1 + product2)
#

# print(product1 + smartphone)
