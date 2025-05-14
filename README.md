# 🍔 McDonald's Style Combo Builder App — v2.0

A professional-grade, modular, and deployable Streamlit app simulating a real McDonald’s ordering kiosk. Includes burger customization, AI-powered combo recommendations, order tracking, testing, CI, and Docker support.

---

## 🚀 Features

### 🛒 Customer App (`app.py`)
- Multi-step ordering UI
- Burger builder (choose + customize toppings)
- Select drink, side, and dessert
- AI-powered “🎲 Surprise Me” combo recommender
- Order review + confirmation screen
- Saves all orders to `data/orders.json`

### 📋 Admin Panel (`admin.py`)
- View all previous orders
- Total order count and revenue

### 🧪 Testing
- Unit tests for builder, combo, and config-based combos
- GitHub Actions CI pipeline for automated testing

### 🐳 Docker Support
- Fully containerized for consistent deployment

---

## 🗂 Folder Structure
```
mcd-menu-app/
├── app.py                 # Main Streamlit customer interface
├── admin.py               # Admin dashboard
├── Dockerfile             # Docker image setup
├── .dockerignore
├── requirements.txt
├── README.md
│
├── data/
│   ├── combo_config.json
│   └── orders.json
│
├── factories/
│   ├── base_factory.py
│   ├── concrete_factories.py
│   └── config_factory.py
│
├── models/
│   ├── base.py
│   ├── builder.py
│   └── combo.py
│
├── tests/
│   ├── test_builder.py
│   ├── test_combo.py
│   └── test_config_factory.py
│
└── .github/workflows/
    └── python-tests.yml
```

---

## ✅ Run the App
```bash
streamlit run app.py
```

To access the admin dashboard:
```bash
streamlit run admin.py
```

---

## 🐳 Run with Docker
```bash
docker build -t mcd-menu-app .
docker run -p 8501:8501 mcd-menu-app
```

---

## 🧪 Run Tests
```bash
pytest tests/
```

---

## 🔁 GitHub CI
Auto-testing with GitHub Actions: `.github/workflows/python-tests.yml`

Badge example:
```markdown
![CI](https://github.com/jaswanth212009/mcd-menu-app/actions/workflows/python-tests.yml/badge.svg)
```

---

## ✨ Version 2.0 Highlights
- [x] Sidebar "Surprise Me" recommender
- [x] Order tracking via JSON
- [x] Kiosk-like multi-step UX
- [x] Dockerfile added
- [x] Full CI/CD via GitHub Actions

---

Built with ❤️ by Jaswanth using Python, Streamlit, Pytest, and a side of fries 🍟
