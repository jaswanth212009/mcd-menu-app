import pytest
from models.builder import BurgerBuilder

def test_add_toppings():
    burger = (
        BurgerBuilder("Big Mac", 5.99)
        .add_cheese()
        .add_bacon()
        .add_egg()
        .add_extra_patty()
        .build()
    )
    assert burger.price == pytest.approx(5.99 + 0.5 + 0.7 + 0.6 + 1.5)
    assert len(burger.toppings) == 4