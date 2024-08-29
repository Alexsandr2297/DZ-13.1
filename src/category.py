from src.product import Product
from src.category_iterator import CategoryIterator


class Category:
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
