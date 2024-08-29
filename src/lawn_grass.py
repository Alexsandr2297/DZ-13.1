from src.product import Product


class LawnGrass(Product):
    """Класс для травы газонной"""
    strange_producer: str  # страна-производитель
    germination_period: int  # срок-прорастания
    color: str  # цвет

    def __init__(self, strange_producer, germination_period, color, title, description, price, quantity):
        """Конструктор для травы газонной"""
        super().__init__(title, description, price, quantity)
        self.strange_producer = strange_producer
        self.germination_period = germination_period
        self.color = color

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
