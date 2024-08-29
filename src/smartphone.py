from src.product import Product


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
