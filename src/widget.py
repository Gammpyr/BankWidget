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


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))

    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Счет 73654108430135874305"))

    print(get_time("2024-03-11T02:26:18.671407"))
