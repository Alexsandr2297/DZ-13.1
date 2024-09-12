import pytest

from src.lawn_grass import LawnGrass


@pytest.fixture()
def lawn_grass():
    return LawnGrass("Italy", 2, "green", "lawn", "Эта трава - "
                                                  "идеальное растение для создания густого и привлекательного газона, "
                                                  "легко выделяющегося на фоне других культур.", 9.999, 5)


def test_init(lawn_grass):
    assert lawn_grass.strange_producer == "Italy"
    assert lawn_grass.germination_period == 2
    assert lawn_grass.color == "green"
    assert lawn_grass.title == "lawn"
    assert lawn_grass.description == "Эта трава - " \
                                     "идеальное растение для создания густого и привлекательного газона, " \
                                     "легко выделяющегося на фоне других культур."
    assert lawn_grass.price == 9.999
    assert lawn_grass.quantity == 5


def test_display_info(lawn_grass, capsys):
    lawn_grass.display_info()
    captured = capsys.readouterr()
    assert captured.out == 'Lawn_grass: lawn, 9.999 Rub, 5 шт, Italy, 2 Месяц, green\n'
