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


class CategoryIterator:
    """Итератор для класса Category"""

    def __init__(self, products):
        """Конструктор для итератора"""
        self._products = products
        self._index = 0

    def __iter__(self):
        """Возвращает сам итератор."""
        return self

    def __next__(self):
        """Возвращает следующий продукт в списке."""
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
