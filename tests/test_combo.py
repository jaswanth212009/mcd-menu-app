import pytest


from models.base import Drink, Side, Dessert

from models.builder import BurgerBuilder
from models.combo import ComboMeal

def test_combo_total():
    burger = BurgerBuilder("Cheese Burger", 4.99).add_cheese().build()
    drink = Drink("Coke", 1.99)
    side = Side("Fries", 2.49)
    dessert = Dessert("Sundae", 2.19)
    combo = ComboMeal(burger, drink, side, dessert)
    total = 4.99 + 0.5 + 1.99 + 2.49 + 2.19
    assert combo.total_price() == pytest.approx(total)