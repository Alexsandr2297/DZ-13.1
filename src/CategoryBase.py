from abc import ABC, abstractmethod


class CategoryBase(ABC):
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def total(self):
        pass
