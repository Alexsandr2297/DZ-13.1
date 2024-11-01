from src.CategoryBase import CategoryBase


class Order(CategoryBase):
    purchased_product: str  # купленный товар
    quantity_purchased_product: int  # количество купленного товара
    total_cost: float  # итоговая стоимость

    def __init__(self, purchased_product, quantity_purchased_product, total_cost, price, quantity):
        super().__init__(price, quantity)
        self.purchased_product = purchased_product
        self.quantity_purchased_product = quantity_purchased_product
        self.total_cost = total_cost

    def __repr__(self):
        return (f"{self.__class__.__name__}: купленный товар: {self.purchased_product}, "
                f"количество купленного товара {self.quantity_purchased_product}, "
                f"итоговая стоимость {self.total_cost}")

    def total(self):
        """Считает стоимость купленного товара"""
        return self.price * self.quantity_purchased_product

# o = Order('Зомби в доме', 10, 19999.99, 1999.99, 10)
# # print(o)
# # print(o.total())
# add_product(o)
