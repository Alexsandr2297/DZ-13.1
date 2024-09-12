from abc import ABC, abstractmethod


class CategoryBase(ABC):

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def total(self):
        pass
