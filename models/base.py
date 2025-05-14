class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        return f" {self.name} - ${self.price:.2f}"
    
class Burger(MenuItem):
    def __init__(self,name, price):
        super().__init__(name, price)
        self.toppings = []

    def add_toppings(self, toppings, cost):
        self.toppings.append((toppings, cost))
        self.price += cost

    def describe(self):
        base = super().describe()
        if self.toppings:
            topping_list = ", ".join(t[0] for t in self.toppings)
            return f" {base} (with {topping_list})"
        return base

class Drink(MenuItem):
    pass

class Side(MenuItem):
    pass

class Dessert(MenuItem):
    pass

