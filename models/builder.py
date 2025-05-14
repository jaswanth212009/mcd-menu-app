from models.base import Burger

class BurgerBuilder:
    def __init__(self, name, base_price):
        self.burger = Burger(name, base_price)

    def add_cheese(self):
        self.burger.add_toppings("cheese", 0.5)
        return self
    
    def add_bacon(self):
        self.burger.add_toppings("bacon", 0.7)
        return self
    
    def add_egg(self):
        self.burger.add_toppings("egg", 0.6)
        return self

    def add_extra_patty(self):
        self.burger.add_toppings("Extra patty", 1.5)
        return self
    
    def build(self):
        return self.burger

