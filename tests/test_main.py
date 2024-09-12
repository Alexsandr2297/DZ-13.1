from src.main import Smartphone, LawnGrass, Product


def test_smartphone():
    phone = Smartphone(2.50, "8 plus", 128, "gray", "iphone",
                       "Apple iPhone 8 Plus поражает своими техническими характеристиками, "
                       "широким набором функций и красивым внешним видом.", 49.999, 2)
    assert phone.efficiency == 2.50
    assert phone.model == "8 plus"
    assert phone.amount_of_internal_memory == 128
    assert phone.color == "gray"
    assert phone.title == "iphone"
    assert phone.description == "Apple iPhone 8 Plus поражает своими техническими характеристиками, " \
                                "широким набором функций и красивым внешним видом."
    assert phone.price == 49.999
    assert phone.quantity == 2


def test_lawn_grass():
    grass = LawnGrass("Italy", 2, "green", "lawn",
                      "Эта трава - идеальное растение для создания густого и привлекательного газона, "
                      "легко выделяющегося на фоне других культур.", 9.999, 5)
    assert grass.strange_producer == "Italy"
    assert grass.germination_period == 2
    assert grass.color == "green"
    assert grass.title == "lawn"
    assert grass.description == "Эта трава - идеальное растение для создания густого и привлекательного газона, " \
                                "легко выделяющегося на фоне других культур."
    assert grass.price == 9.999
    assert grass.quantity == 5


def test_product():
    product = Product('Зомби в доме', 'Для веселого времяпровождения в компании', 1999.99, 10)
    assert product.title == 'Зомби в доме'
    assert product.description == 'Для веселого времяпровождения в компании'
    assert product.price == 1999.99
    assert product.quantity == 10
