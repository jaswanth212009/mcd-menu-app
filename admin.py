# File: admin.py (View Orders Page)
import streamlit as st
import json
import os

st.set_page_config(page_title="🍟 Admin - View Orders", layout="centered")
st.title("📋 Order History Dashboard")

orders_path = "data/orders.json"

if not os.path.exists(orders_path):
    st.warning("No orders have been placed yet.")
else:
    with open(orders_path, "r") as f:
        orders = json.load(f)

    st.subheader(f"Total Orders: {len(orders)}")

    total_sales = sum(order["total"] for order in orders)
    st.subheader(f"💰 Total Sales: ${total_sales:.2f}")

    st.divider()
    for i, order in enumerate(orders[::-1], 1):  # show latest first
        with st.expander(f"📦 Order #{len(orders) - i + 1}"):
            st.markdown(f"**Burger**: {order['burger']}")
            st.markdown(f"**Drink**: {order['drink']}")
            st.markdown(f"**Side**: {order['side']}")
            st.markdown(f"**Dessert**: {order['dessert']}")
            st.markdown(f"**Total**: ${order['total']:.2f}")
