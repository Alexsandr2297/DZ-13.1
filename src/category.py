from abc import ABC

from src.CategoryBase import CategoryBase
from src.category_iterator import CategoryIterator
from src.product import Product


class Category(CategoryBase, ABC):
    """Класс для Категории"""
    title: str  # Название
    description: str  # Описание
    products: list  # Товары
    total_number_of_categories = 0  # общее количество категорий.
    total_number_of_unique_products = 0  # общее количество уникальных продуктов.

    def __init__(self, title, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.title = title
        self.description = description
        self.__products = products
        Category.total_number_of_categories += 1
        Category.total_number_of_unique_products += len(self.__products)

    def add_products(self, product):
        """Добавляет продукт в категорию."""
        if isinstance(product, Product):
            return self.__products.append(product)
        raise TypeError("В класс Product можно добавлять только их подклассы")

    @property
    def products(self):
        """Возвращает список строк с информацией о продуктах в категории."""
        return [f"{product.title}, {product.price} руб. Остаток:{product.quantity} шт." for product in
                self.__products]

    def __str__(self):
        """"Возвращает строковое представление категории."""
        product_count = len(self.__products)
        self.category_name = self.title
        return f'{self.category_name}, количество продуктов: {product_count} шт.'

    def __iter__(self):
        """"Возвращает итератор для обхода продуктов в категории."""
        return CategoryIterator(self.__products)

    def __repr__(self):
        return f"{self.__class__.__name__}, {self.title}, {self.description}, {self.products}"

    def total(self):
        """Возвращает общую стоимость всех продуктов в категории."""
        return sum(product.price * product.quantity for product in self.__products)

# category1 = Category('Настольные игры', 'Для веселого времяпровождения в компании',
#                      [Product('Зомби в доме', 'Для веселого времяпровождения в компании', 1999.99, 10),
#                       Product('Имаджинариум', 'Для веселого времяпровождения в компании', 2999.99, 5),
#                       Product('Экивоки', 'Для веселого времяпровождения в компании', 3999.99, 3)])
# print(category1.__repr__())
# print(category1.total())
