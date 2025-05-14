# File: factories/config_factory.py (with debug prints)
import json
from models.base import Drink, Side, Dessert
from models.builder import BurgerBuilder
from models.combo import ComboMeal

class ConfigComboFactory:
    def __init__(self, config_path):
        print(f"📁 Loading combo config from: {config_path}")
        with open(config_path, 'r') as f:
            self.combos = json.load(f)
        print(f"✅ Loaded combos: {list(self.combos.keys())}")

    def create_combo(self, combo_name):
        print(f"🔍 Creating combo: {combo_name}")

        if combo_name not in self.combos:
            raise ValueError(f"❌ Combo '{combo_name}' not found in config")

        data = self.combos[combo_name]

        # Build burger
        burger_data = data["burger"]
        print(f"🍔 Building burger: {burger_data['name']} @ ${burger_data['price']:.2f}")
        builder = BurgerBuilder(burger_data["name"], burger_data["price"])

        for topping in burger_data.get("toppings", []):
            method = topping.replace(" ", "_").lower()
            if hasattr(builder, f"add_{method}"):
                print(f"   ➕ Adding topping: {topping}")
                getattr(builder, f"add_{method}")()
            else:
                print(f"   ⚠️ Skipping unknown topping: {topping}")

        burger = builder.build()

        # Build drink
        drink_data = data["drink"]
        print(f"🥤 Creating drink: {drink_data['name']} @ ${drink_data['price']:.2f}")
        drink = Drink(**drink_data)

        # Build side
        side_data = data["side"]
        print(f"🍟 Creating side: {side_data['name']} @ ${side_data['price']:.2f}")
        side = Side(**side_data)

        # Build dessert
        dessert_data = data["dessert"]
        print(f"🍦 Creating dessert: {dessert_data['name']} @ ${dessert_data['price']:.2f}")
        dessert = Dessert(**dessert_data)

        print("✅ Combo successfully built!")
        return ComboMeal(burger, drink, side, dessert)
