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
