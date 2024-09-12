from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def main():
    Smartphone(2.50, "8 plus", 128, "gray", "iphone",
               "Apple iPhone 8 Plus поражает своими техническими характеристиками, "
               "широким набором функций и красивым внешним видом.", 49.999, 2)

    LawnGrass("Italy", 2, "green", "lawn", "Эта трава - "
                                           "идеальное растение для создания густого и привлекательного газона, "
                                           "легко выделяющегося на фоне других культур.", 9.999, 5)
    Product('Зомби в доме', 'Для веселого времяпровождения в компании', 1999.99, 10)


if __name__ == "main":
    main()
