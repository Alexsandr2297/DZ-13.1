from abc import ABC

from src.product import Product


class Smartphone(Product, ABC):
    """Класс для смартфона"""
    efficiency: float  # производительность
    model: str  # модель
    amount_of_internal_memory: int  # объем встроенной памяти
    color: str  # цвет

    def __init__(self, efficiency, model, amount_of_internal_memory, color, title, description, price, quantity):
        """Конструктор для смартфона"""

        self.efficiency = efficiency
        self.model = model
        self.amount_of_internal_memory = amount_of_internal_memory
        self.color = color
        super().__init__(title, description, price, quantity)

    def display_info(self):
        """Выводит информацию по продукту"""
        print(
            f"Smartphone: {self.efficiency}ГГц, {self.model}, "
            f"{self.amount_of_internal_memory}ГБ, {self.color}, {self.price} Rub, {self.quantity} шт")


iphone = Smartphone(2.50, "8 plus", 128, "gray", "iphone",
                    "Apple iPhone 8 Plus поражает своими техническими характеристиками, "
                    "широким набором функций и красивым внешним видом.", 49.999, 2)
# iphone.display_info()
# sma2 = LawnGrass("Italy", 2, "green", "lawn", "Эта трава - "
#                                               "идеальное растение для создания густого и привлекательного газона, "
#                                               "легко выделяющегося на фоне других культур.", 9.999, 5)

# sma.display_info()
# print(Smartphone.__mro__)
