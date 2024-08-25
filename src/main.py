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
        self.__products.append(product)

    @property
    def products(self):
        return [f"{product.title}, {product.price} руб. Остаток:{product.quantity} шт." for product in
                self.__products]

    def __str__(self):
        product_count = len(self.__products)
        self.category_name = self.title
        return f'{self.category_name}, количество продуктов: {product_count} шт.'

    def __iter__(self):
        return CategoryIterator(self.__products)


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

    @classmethod
    def product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)

    def __str__(self):
        return f"{self.title}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return (self.price * self.quantity) + (other.price * other.quantity)


class CategoryIterator:
    """Итератор для класса Category"""

    def __init__(self, products):
        self._products = products
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._products):
            product = self._products[self._index]
            self._index += 1
            return product
        else:
            raise StopIteration


class Smartphone(Product):
    """Класс для смартфона"""
    efficiency: float  # производительность
    model: str  # модель
    amount_of_internal_memory: int  # объем встроенной памяти
    color: str  # цвет

    def __init__(self, efficiency, model, amount_of_internal_memory, color, title, description, price, quantity):
        """Конструктор для смартфона"""
        super().__init__(title, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.amount_of_internal_memory = amount_of_internal_memory
        self.color = color

    def __add__(self, other):
        if type(self) is type(other):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError


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

product1 = Product('Зомби в доме', 'Для веселого времяпровождения в компании', 1999.99, 10)
product2 = Product('Имаджинариум', 'Для веселого времяпровождения в компании', 2999.99, 5)
print(product1 + product2)

smartphone = Smartphone(2.50, "iphone 8 plus", 128, "grea", "smarthone",
                        "ok", 1.999, 2)
print(product1 + smartphone)
