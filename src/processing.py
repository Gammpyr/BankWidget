def filter_by_state(dict_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state и возвращает новый список словарей,
    у которых ключ state соответствует указанному значению."""
    result = []
    for data in dict_list:
        if data:
            if data["state"] == state:
                result.append(data)
    return result


def sort_by_date(dict_list: list[dict], sort_order: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки.
    И возвращает новый список, отсортированный по дате"""
    sorted_result = sorted(dict_list, key=lambda x: x["date"], reverse=sort_order)
    return sorted_result
