# File: app.py (Multi-step McD Kiosk UI)
import streamlit as st
from models.builder import BurgerBuilder
from models.base import Drink, Side, Dessert
from models.combo import ComboMeal
import json
import os

# Initialize Streamlit session state
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'burger_name' not in st.session_state:
    st.session_state.burger_name = None
if 'burger_price' not in st.session_state:
    st.session_state.burger_price = 0.0
if 'toppings' not in st.session_state:
    st.session_state.toppings = []
if 'drink_name' not in st.session_state:
    st.session_state.drink_name = None
if 'drink_price' not in st.session_state:
    st.session_state.drink_price = 0.0
if 'side_name' not in st.session_state:
    st.session_state.side_name = None
if 'side_price' not in st.session_state:
    st.session_state.side_price = 0.0
if 'dessert_name' not in st.session_state:
    st.session_state.dessert_name = None
if 'dessert_price' not in st.session_state:
    st.session_state.dessert_price = 0.0

st.title("🍔 McDonald's Kiosk")

# Step 1: Choose Burger
if st.session_state.step == 1:
    st.header("Step 1: Choose Your Burger")
    burgers = {
        "Big Mac": 5.99,
        "McSpicy Chicken": 6.49,
        "Cheese Burger": 4.99
    }
    burger_name = st.selectbox("Select a burger:", list(burgers.keys()))
    st.session_state.burger_name = burger_name
    st.session_state.burger_price = burgers[burger_name]

    if st.button("Next →"):
        st.session_state.step = 2
        st.rerun()

# Step 2: Add Toppings
elif st.session_state.step == 2:
    st.header("Step 2: Customize Toppings")
    toppings = []
    if st.checkbox("🧀 Cheese (+$0.50)"):
        toppings.append("cheese")
    if st.checkbox("🥓 Bacon (+$0.70)"):
        toppings.append("bacon")
    if st.checkbox("🍳 Egg (+$0.60)"):
        toppings.append("egg")
    if st.checkbox("🍔 Extra Patty (+$1.50)"):
        toppings.append("extra patty")
    st.session_state.toppings = toppings

    if st.button("← Back"):
        st.session_state.step = 1
        st.rerun()
    if st.button("Next →"):
        st.session_state.step = 3
        st.rerun()

# Step 3: Choose Drink
elif st.session_state.step == 3:
    st.header("Step 3: Choose Your Drink")
    drinks = {
        "Coke": 1.99,
        "Sprite": 1.99,
        "Coffee": 2.49,
        "Water": 0.99
    }
    drink_name = st.selectbox("Select a drink:", list(drinks.keys()))
    st.session_state.drink_name = drink_name
    st.session_state.drink_price = drinks[drink_name]

    if st.button("← Back"):
        st.session_state.step = 2
        st.rerun()
    if st.button("Next →"):
        st.session_state.step = 4
        st.rerun()

# Step 4: Choose Side and Dessert
elif st.session_state.step == 4:
    st.header("Step 4: Choose Your Side and Dessert")

    sides = {
        "Fries": 2.49,
        "Spicy Nuggets": 2.99,
        "Hash Brown": 2.29
    }
    side_name = st.selectbox("Select a side:", list(sides.keys()))
    st.session_state.side_name = side_name
    st.session_state.side_price = sides[side_name]

    desserts = {
        "Vanilla Cone": 1.29,
        "McFlurry": 2.49,
        "Sundae": 2.19
    }
    dessert_name = st.selectbox("Select a dessert:", list(desserts.keys()))
    st.session_state.dessert_name = dessert_name
    st.session_state.dessert_price = desserts[dessert_name]

    if st.button("← Back"):
        st.session_state.step = 3
        st.rerun()
    if st.button("Next →"):
        st.session_state.step = 5
        st.rerun()

# Step 5: Review and Confirm Order
elif st.session_state.step == 5:
    st.header("Step 5: Review and Confirm")
    burger_builder = BurgerBuilder(st.session_state.burger_name, st.session_state.burger_price)
    for topping in st.session_state.toppings:
        method = topping.replace(" ", "_").lower()
        if hasattr(burger_builder, f"add_{method}"):
            getattr(burger_builder, f"add_{method}")()
    burger = burger_builder.build()

    drink = Drink(st.session_state.drink_name, st.session_state.drink_price)
    side = Side(st.session_state.side_name, st.session_state.side_price)
    dessert = Dessert(st.session_state.dessert_name, st.session_state.dessert_price)

    combo = ComboMeal(burger, drink, side, dessert)
    st.markdown(combo.describe())

    if st.button("← Back"):
        st.session_state.step = 4
        st.rerun()

    if st.button("✅ Confirm and Place Order"):
        order = {
            "burger": burger.describe(),
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

        st.success("🎉 Order placed successfully!")
        st.balloons()
        st.session_state.step = 1
        st.rerun()
