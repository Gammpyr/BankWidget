import re
from collections import Counter


def filter_transactions_by_description(dict_list: list[dict], search_str: str) -> list[dict]:
    """Принимает список с транзакциями и строку,
    и возвращает список транзакций содержащих в описании эту строку"""
    result = list()
    for transaction in dict_list:
        if isinstance(transaction["description"], str):
            search_result = re.search(search_str.lower(), transaction["description"].lower())
            if search_result:
                result.append(transaction)
    return result


def count_transactions_by_description(dict_list: list[dict], my_category_list: list[str]) -> dict:
    """Принимает список транзакций и список категорий.
    Подсчитывает и возвращает количество указанных категорий среди транзакций"""
    my_category_set = set(my_category_list)
    category_list = [
        transaction["description"]
        for transaction in dict_list
        if isinstance(transaction["description"], str) and transaction["description"] in my_category_set
    ]

    counted_category = Counter(category_list).most_common(len(my_category_set))

    result = dict()
    for category, counter in counted_category:
        result[category] = counter

    return result
