import json
import logging
from datetime import datetime
from typing import Any

from src.external_api import convert_to_rub

file_logger = logging.getLogger("utils")
file_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8")
file_logger.addHandler(file_handler)
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)


def get_data_from_json(path: str) -> Any:
    """Получает путь к файлу json и возвращает словарь с данными"""
    file_logger.info("Начинает работу функция get_data_from_json")
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        file_logger.info(f"Открываем файл по пути {path}")
    except FileNotFoundError as ex:
        file_logger.error(f"Ошибка при открытии: {ex}")
        return []
    if not data or not isinstance(data, list):
        file_logger.warning("Файл пустой")
        return []
    else:
        file_logger.info("Возвращаем файл")
        file_logger.info("Завершена работа функции get_data_from_json")
        return data


def get_amount_in_rubles(transaction: dict) -> Any:
    """
    Получает словарь с транзакцией и возвращает сумму транзакции.
    Если валюта отличается от RUB, сначала конвертирует в RUB
    """
    # file_logger.info(f'Начинает работу функция get_amount_in_rubles')

    if not transaction:
        file_logger.warning("Полученная транзакция пуста")
        return None

    code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]

    if code == "RUB":
        file_logger.warning("Получена транзакция в рублях")
        return amount

    try:
        file_logger.info(f"Открываем файла {code}.json")
        with open(f"data/{code}.json") as f:
            rate_data = json.load(f)
    except FileNotFoundError as ex:
        file_logger.error(f"Ошибка {ex}")
        return convert_to_rub(code, amount)
    else:
        today_date = datetime.now().strftime("%Y-%m-%d")
        file_logger.info(f"Проверка текущей даты в файле {code}.json")
        if today_date == rate_data["date"]:
            rate = rate_data["info"]["rate"]
            file_logger.info(f"Используем данные из файла {code}.json")
            return rate * float(amount)
        else:
            file_logger.info(f"Конвертируем {code} в RUB")
            return convert_to_rub(code, amount)
