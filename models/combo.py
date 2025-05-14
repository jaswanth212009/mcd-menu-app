class ComboMeal:
    def __init__(self, burger, drink, side, dessert):
        self.burger = burger
        self.drink = drink
        self.side = side
        self.dessert = dessert

    def total_price(self):
        return self.burger.price + self.drink.price + self.side.price + self.dessert.price
    
    
    def describe(self):
        return (
            f" Combo Meal:\n"
            f"🍔 {self.burger.describe()}\n"
            f"🥤 {self.drink.describe()}\n"
            f"🍟 {self.side.describe()}\n"
            f"🍦 {self.dessert.describe()}\n"
            f"💰 Total: ${self.total_price():.2f}"
        )