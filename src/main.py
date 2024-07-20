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
        self.products = products


class Product:
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
