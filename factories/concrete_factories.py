from models.base import  Drink, Side, Dessert
from factories.base_factory import ComboFactory
from models.builder import BurgerBuilder

class ClassicComboFactory(ComboFactory):
    def create_burger(self):
        return BurgerBuilder("Big Mac", 5.99).add_cheese().build()
    
    def create_drink(self):
        return Drink("Coke", 1.99)
    
    def create_side(self):
        return Side("Fries", 2.49)
    
    def create_dessert(self):
        return Dessert("Vanilla Cone", 1.29)
    
class SpicyComboFactory(ComboFactory):
    def create_burger(self):
        return BurgerBuilder("McSpicy Chicken", 6.49).add_extra_patty().add_egg().build()
    
    def create_drink(self):
        return Drink("Sprite", 1.99)
    
    def create_side(self):
        return Side("Spicy Nuggets", 2.99)
    
    def create_dessert(self):
        return Dessert("McFlurry", 2.49)