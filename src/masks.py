def get_mask_card_number(card_number: int | str) -> str:
    """Принимает номер карты, возвращает её маску"""
    number_list = str(card_number)
    result = f"{number_list[:4]} {number_list[4:6]}** **** {number_list[-4:]}"
    return result


def get_mask_account(account_number: int | str) -> str:
    """Принимает номер счета и возвращает маску формата **XXXX"""
    str_account_number = str(account_number)
    return f"**{str_account_number[-4:]}"
