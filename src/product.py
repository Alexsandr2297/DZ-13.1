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
