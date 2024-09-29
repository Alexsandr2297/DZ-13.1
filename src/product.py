from abc import ABC

from src.ProductBase import ProductBase
from src.repr_mixin import MixinRepr


class Product(ProductBase, ABC, MixinRepr):
    """Класс для Продукта"""
    title: str  # Название
    description: str  # Описание
    price: float  # Цена
    quantity: int  # количество в наличии

    def __init__(self, title, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""

        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()
        if self.quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

    @classmethod
    def product(cls, name, description, price, quantity):
        """"Создает новый экземпляр продукта."""
        return cls(name, description, price, quantity)

    def __str__(self):
        """Возвращает строковое представление продукта."""
        return f"{self.title}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение двух продуктов по цене и количеству, если оба продукта одного класса"""
        if type(self) is type(other):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError(f"Нельзя добовлять продукт к смартфону: {type(self).__name__} и {type(other).__name__}")

    def display_info(self):
        """Выводит информацию попродукту"""
        print(f"Product: {self.title}, {self.price}, {self.quantity}")


# try:
#     product1 = Product('Зомби в доме', 'Для веселого времяпровождения в компании', 1999.99, 0)
# except ValueError as e:
#     print(e)

