from src.transaction_filtering import count_transactions_by_description, filter_transactions_by_description

dict_for_test = [
    {
        "description": "Перевод организации",
    },
    {
        "description": "Перевод организации",
    },
    {
        "description": "Открытие вклада",
    },
    {
        "description": "Перевод со счета на счет",
    },
]

expected_filter = [{"description": "Перевод организации"}, {"description": "Перевод организации"}]


def test_filter_transactions_by_description() -> None:
    assert filter_transactions_by_description(dict_for_test, "Перевод организации") == expected_filter
    assert filter_transactions_by_description(dict_for_test, "123") == []
    assert filter_transactions_by_description(dict_for_test, "") == dict_for_test


category_list = [
    "Открытие вклада",
    "Перевод организации",
    "Перевод со счета на счет",
    "Перевод с карты на карту",
]

expected_count = {"Перевод организации": 2, "Открытие вклада": 1, "Перевод со счета на счет": 1}


def test_count_transactions_by_description() -> None:
    assert count_transactions_by_description(dict_for_test, category_list) == expected_count
    assert count_transactions_by_description(dict_for_test, ["123"]) == {}
    assert count_transactions_by_description(dict_for_test, []) == {}
