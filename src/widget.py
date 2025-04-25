from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Функция определяет тип карты/счёта и возвращает соответствующую маску"""
    if "Счет" in card_info:
        account_mask = "Счет " + get_mask_account(card_info[5:])
        return account_mask
    else:
        card_mask = card_info[:-16] + get_mask_card_number(card_info[-16:])
        return card_mask


def get_time(date: str) -> str:
    """Функция получает время и возвращает в формате ДД.ММ.ГГГГ"""
    get_datetime = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    correct_date = get_datetime.strftime("%d.%m.%Y")
    return correct_date
