from abc import ABC, abstractmethod


class ProductBase(ABC):
    @abstractmethod
    def display_info(self):
        pass
