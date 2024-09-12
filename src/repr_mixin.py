class MixinRepr:

    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f"Создан класс: {self.__class__.__name__}({self.__dict__.items()})"
