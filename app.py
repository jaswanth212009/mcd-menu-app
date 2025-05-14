# File: app.py (fully working with Surprise Me)
import streamlit as st
import json
import os
import random
from models.builder import BurgerBuilder
from models.base import Drink, Side, Dessert
from models.combo import ComboMeal

st.set_page_config(page_title="🍔 McDonald's Kiosk", layout="centered")
st.title("🍔 McDonald's Combo Builder")

# Set price dictionaries
burger_prices = {"Big Mac": 5.99, "McSpicy Chicken": 6.49, "Cheese Burger": 4.99}
drink_prices = {"Coke": 1.99, "Sprite": 1.99, "Coffee": 2.49, "Water": 0.99}
side_prices = {"Fries": 2.49, "Spicy Nuggets": 2.99, "Hash Brown": 2.29}
dessert_prices = {"Vanilla Cone": 1.29, "McFlurry": 2.49, "Sundae": 2.19}

# Sidebar AI Suggestion
with st.sidebar:
    st.markdown("### 🤖 Surprise Me!")
    if st.button("🎲 Suggest Combo"):
        st.session_state.burger_name = random.choice(list(burger_prices))
        st.session_state.burger_price = burger_prices[st.session_state.burger_name]
        st.session_state.toppings = random.sample(
            ["cheese", "bacon", "egg", "extra patty"],
            k=random.randint(0, 2)
        )
        st.session_state.drink_name = random.choice(list(drink_prices))
        st.session_state.drink_price = drink_prices[st.session_state.drink_name]
        st.session_state.side_name = random.choice(list(side_prices))
        st.session_state.side_price = side_prices[st.session_state.side_name]
        st.session_state.dessert_name = random.choice(list(dessert_prices))
        st.session_state.dessert_price = dessert_prices[st.session_state.dessert_name]
        st.session_state.step = 5
        st.rerun()

# Init session state
for key, default in {
    'step': 1,
    'burger_name': None,
    'burger_price': 0.0,
    'toppings': [],
    'drink_name': None,
    'drink_price': 0.0,
    'side_name': None,
    'side_price': 0.0,
    'dessert_name': None,
    'dessert_price': 0.0
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# Step 1: Choose Burger
if st.session_state.step == 1:
    st.header("Step 1: Choose Your Burger")
    st.session_state.burger_name = st.selectbox("Select a burger:", list(burger_prices))
    st.session_state.burger_price = burger_prices[st.session_state.burger_name]
    if st.button("Next →"):
        st.session_state.step = 2
        st.rerun()

# Step 2: Add Toppings
elif st.session_state.step == 2:
    st.header("Step 2: Customize Toppings")
    selected_toppings = []
    for topping in ["cheese", "bacon", "egg", "extra patty"]:
        if st.checkbox(f"Add {topping}"):
            selected_toppings.append(topping)
    st.session_state.toppings = selected_toppings
    col1, col2 = st.columns(2)
    if col1.button("← Back"):
        st.session_state.step = 1
        st.rerun()
    if col2.button("Next →"):
        st.session_state.step = 3
        st.rerun()

# Step 3: Drink
elif st.session_state.step == 3:
    st.header("Step 3: Choose Your Drink")
    st.session_state.drink_name = st.selectbox("Select a drink:", list(drink_prices))
    st.session_state.drink_price = drink_prices[st.session_state.drink_name]
    col1, col2 = st.columns(2)
    if col1.button("← Back"):
        st.session_state.step = 2
        st.rerun()
    if col2.button("Next →"):
        st.session_state.step = 4
        st.rerun()

# Step 4: Side + Dessert
elif st.session_state.step == 4:
    st.header("Step 4: Choose Side and Dessert")
    st.session_state.side_name = st.selectbox("Select a side:", list(side_prices))
    st.session_state.side_price = side_prices[st.session_state.side_name]
    st.session_state.dessert_name = st.selectbox("Select a dessert:", list(dessert_prices))
    st.session_state.dessert_price = dessert_prices[st.session_state.dessert_name]
    col1, col2 = st.columns(2)
    if col1.button("← Back"):
        st.session_state.step = 3
        st.rerun()
    if col2.button("Next →"):
        st.session_state.step = 5
        st.rerun()

# Step 5: Review & Confirm
elif st.session_state.step == 5:
    st.header("Step 5: Review and Confirm")
    burger = BurgerBuilder(st.session_state.burger_name, st.session_state.burger_price)
    for t in st.session_state.toppings:
        getattr(burger, f"add_{t.replace(' ', '_')}")()
    final_burger = burger.build()
    drink = Drink(st.session_state.drink_name, st.session_state.drink_price)
    side = Side(st.session_state.side_name, st.session_state.side_price)
    dessert = Dessert(st.session_state.dessert_name, st.session_state.dessert_price)
    combo = ComboMeal(final_burger, drink, side, dessert)
    st.markdown(combo.describe())
    col1, col2 = st.columns(2)
    if col1.button("← Back"):
        st.session_state.step = 4
        st.rerun()
    if col2.button("✅ Confirm Order"):
        order = {
            "burger": final_burger.describe(),
            "drink": drink.describe(),
            "side": side.describe(),
            "dessert": dessert.describe(),
            "total": combo.total_price()
        }
        os.makedirs("data", exist_ok=True)
        orders_path = "data/orders.json"
        if os.path.exists(orders_path):
            with open(orders_path, "r") as f:
                orders = json.load(f)
        else:
            orders = []
        orders.append(order)
        with open(orders_path, "w") as f:
            json.dump(orders, f, indent=2)
        st.success("🎉 Order placed!")
        st.balloons()
        st.session_state.step = 1
        st.rerun()
