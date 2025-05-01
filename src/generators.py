from typing import Generator


def filter_by_currency(transactions_list: list[dict], value: str) -> Generator[dict]:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    try:
        for data in transactions_list:
            if data["operationAmount"]["currency"]["code"] == value:
                yield data
    except KeyError:
        for data in transactions_list:
            if data["currency_code"] == value:
                yield data


def transaction_descriptions(transactions_list: list[dict]) -> Generator[str | None]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции, по очереди"""
    if not transactions_list:
        yield None
    for data in transactions_list:
        yield data["description"]


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    num = start
    while num <= stop:
        card_number_len = "0000000000000000"
        edited_number = card_number_len[: -len(str(num))] + str(num)
        result = f"{edited_number[:4]} {edited_number[4:8]} {edited_number[8:12]} {edited_number[12:16]}"
        yield result
        num += 1
