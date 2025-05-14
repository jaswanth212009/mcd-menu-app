import json
import pytest
from factories.config_factory import ConfigComboFactory
from models.combo import ComboMeal

@pytest.fixture
def sample_config(tmp_path):
    data = {
        "test_combo": {
            "burger": {
                "name": "Test Burger",
                "price": 5.0,
                "toppings": ["cheese", "egg"]
            },
            "drink": {"name": "Water", "price": 0.99},
            "side": {"name": "Hash Brown", "price": 1.5},
            "dessert": {"name": "Sundae", "price": 2.0}
        }
    }
    file_path = tmp_path / "config.json"
    with open(file_path, "w") as f:
        json.dump(data, f)
    return file_path

def test_config_factory_load(sample_config):
    factory = ConfigComboFactory(str(sample_config))
    combo = factory.create_combo("test_combo")
    assert isinstance(combo, ComboMeal)
    assert combo.total_price() > 0