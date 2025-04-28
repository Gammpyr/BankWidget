import logging

file_logger = logging.getLogger("masks")
file_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8")
file_logger.addHandler(file_handler)
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)


def get_mask_card_number(card_number: int | str) -> str:
    """Принимает номер карты, возвращает её маску"""
    file_logger.info("Начинает работу функция get_mask_card_number")
    try:
        number_list = str(card_number)
        result = f"{number_list[:4]} {number_list[4:6]}** **** {number_list[-4:]}"
        file_logger.info("Завершена работа функции get_mask_card_number")
        return result
    except Exception as ex:
        file_logger.error(f"Ошибка {ex}")
        return ""


def get_mask_account(account_number: int | str) -> str:
    """Принимает номер счета и возвращает маску формата **XXXX"""
    file_logger.info("Начинает работу функция get_mask_account")
    try:
        str_account_number = str(account_number)
        file_logger.info("Завершена работа функции get_mask_account")
        return f"**{str_account_number[-4:]}"
    except Exception as ex:
        file_logger.error(f"Ошибка {ex}")
        return ""
