from factories.config_factory import ConfigComboFactory


if __name__ == "__main__":
    config_path = "data/combo_config.json"
    factory = ConfigComboFactory(config_path)

    combo_names = ['classic_combo', "spicy_combo", "classic_combo"]
    for name in combo_names:
        combo = factory.create_combo(name)
        print(combo.describe())
        print("\n" + "=" * 40 + '\n')