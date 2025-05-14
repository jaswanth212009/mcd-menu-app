import json
from models.base import Drink, Side, Dessert
from models.builder import BurgerBuilder
from models.combo import ComboMeal

class ConfigComboFactory:
    def __init__(self, config_path):
        with open(config_path , 'r') as f:
            self.combos = json.load(f)

    def create_combo(self, combo_name):
        if combo_name not in self.combos:
            raise ValueError(f"Combo '{combo_name}' not found in config")
        
        data = self.combos[combo_name]

        # Build burger using builder

        burger_data = data["burger"]
        builder = BurgerBuilder(burger_data["name"], burger_data["price"])
        for topping in burger_data.get("toppings", []):
            method = topping.replace(" ", "_").lower()
            if hasattr(builder, f"add_{method}"):
                getattr(builder, f"add_{method}")()
        burger = builder.build()

        drink = Drink(**data["drink"])
        side = Side(**data["side"])
        dessert = Dessert(**data["dessert"])

        return ComboMeal(burger, drink, side, dessert)

