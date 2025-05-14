# File: README.md

# 🍔 McDonald's Style Combo Builder App

A full-stack, test-driven, McDonald's-style kiosk app where users can:

- Build combo meals step by step
- Customize burgers with toppings
- Choose drinks, sides, and desserts
- View and track all orders
- Run automated tests with GitHub Actions

---

## 📦 Project Structure
```
mcd_menu_app/
├── app.py                  # Streamlit UI for customers
├── admin.py                # Admin dashboard to view orders
├── data/
│   ├── combo_config.json   # (optional) menu config
│   └── orders.json         # saved customer orders
├── models/                 # Core product classes
│   ├── base.py             # MenuItem, Burger, Drink, etc.
│   ├── builder.py          # BurgerBuilder
│   └── combo.py            # ComboMeal class
├── factories/              # Combo generators
│   ├── base_factory.py
│   ├── concrete_factories.py
│   └── config_factory.py
├── tests/                  # Unit tests (pytest)
│   ├── test_builder.py
│   ├── test_combo.py
│   └── test_config_factory.py
├── requirements.txt        # Python dependencies
└── .github/workflows/      # GitHub Actions
    └── python-tests.yml    # CI pipeline
```

---

## 🚀 Run the App
```bash
streamlit run app.py
```

To view orders:
```bash
streamlit run admin.py
```

---

## 🧪 Run Tests
```bash
pytest tests/
```

---

## ✅ GitHub Actions CI
Automatically runs tests on each push to `main`. See `.github/workflows/python-tests.yml`.

You can add a badge like this to your README (once pushed to GitHub):
```markdown
![CI](https://github.com/<your-username>/<your-repo>/actions/workflows/python-tests.yml/badge.svg)
```

---

## 📬 Want to Add More?
- [ ] Streamlit Cloud Deployment
- [ ] Email Receipt Feature
- [ ] Image Uploads for Menu Items
- [ ] Database Integration

---
Built with ❤️ using Python, Streamlit, and Pytest.
