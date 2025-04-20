import json
from datetime import datetime
from typing import Any

from src.external_api import convert_to_rub

PATH_TO_FILE = "../data/operations.json"


def get_data_from_json(path: str) -> Any:
    """Получает путь к файлу json и возвращает словарь с данными"""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    if not data or isinstance(data, list):
        return []
    else:
        return data


def get_amount_in_rubles(transaction: dict) -> Any:
    """
    Получает словарь с транзакцией и возвращает сумму транзакции.
    Если валюта отличается от RUB, сначала конвертирует в RUB
    """
    if not transaction:
        return None

    code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]

    if code != "RUB":
        try:
            with open(f"../data/{code}.json") as f:
                rate_data = json.load(f)
        except FileNotFoundError:
            return convert_to_rub(code, amount)
        else:
            today_date = datetime.now().strftime("%Y-%m-%d")
            if today_date == rate_data["date"]:
                rate = rate_data["info"]["rate"]
                return rate * float(amount)
            else:
                return convert_to_rub(code, amount)
    else:
        return amount
