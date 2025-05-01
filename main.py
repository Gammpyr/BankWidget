from datetime import datetime
from typing import Any

from src.config import PATH_TO_CSV_FILE, PATH_TO_JSON_FILE, PATH_TO_XLSX_FILE
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.tabular_data import get_data_from_csv_file, get_data_from_excel_file
from src.transaction_filtering import filter_transactions_by_description
from src.utils import get_data_from_json
from src.widget import mask_account_card


def get_clarifications() -> Any:
    """Выводит следующие вопросы для уточнения выборки операций, необходимых пользователю,
    и выводит в консоль операции, соответствующие выборке пользователя"""
    # Пользователь выбирает расширение файла с транзакциями
    while True:
        user_input = input(
            """
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
-> """
        )
        if user_input == "1":
            print("\n   Для обработки выбран JSON-файл.")
            file_data = get_data_from_json(PATH_TO_JSON_FILE)
            file_type = "JSON"
            break
        elif user_input == "2":
            print("\n   Для обработки выбран CSV-файл.")
            file_data = get_data_from_csv_file(PATH_TO_CSV_FILE)
            file_type = "CSV"
            break
        elif user_input == "3":
            print("\n   Для обработки выбран XLSX-файл.")
            file_data = get_data_from_excel_file(PATH_TO_XLSX_FILE)
            file_type = "XLSX"
            break

    # Пользователь выбирает статус интересующих его операций
    while True:
        user_input = input(
            "\nВведите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтрации статусы: EXECUTED, CANCELED, PENDING\n->"
        )

        if user_input.upper() == "EXECUTED":
            print("\n   Операции отфильтрованы по статусу 'EXECUTED'\n")
            state = "EXECUTED"
            break
        elif user_input.upper() == "CANCELED":
            print("\n   Операции отфильтрованы по статусу 'CANCELED'\n")
            state = "CANCELED"
            break
        elif user_input.upper() == "PENDING":
            print("\n   Операции отфильтрованы по статусу 'PENDING'\n")
            state = "PENDING"
            break
        else:
            print(f'\n   Статус операции "{user_input}" недоступен.')

    user_input = input("Отсортировать операции по дате? Да/Нет \n-> ")
    if user_input.lower() == "да":
        is_sort_by_date = True
    else:
        is_sort_by_date = False

    if is_sort_by_date:
        while True:
            user_input = input("Отсортировать дату по возрастанию или по убыванию? (возр\убыв)\n-> ")
            if user_input.lower() in ["возр", "возрастанию", "по возрастанию"]:
                is_sort_by_ascending = False
                break
            elif user_input.lower() in ["убыв", "убыванию", "по убыванию"]:
                is_sort_by_ascending = True
                break
    else:
        is_sort_by_ascending = True

    user_input = input("Выводить только рублевые транзакции? Да/Нет\n-> ")
    if user_input.lower() == "да":
        is_rub_transaction_only = True
    else:
        is_rub_transaction_only = False

    user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n-> ")
    if user_input.lower() == "да":
        filter_by_spec_word = input("Введите слово для фильтрации:\n-> ")
    else:
        filter_by_spec_word = "False"

    return (
        file_data,
        file_type,
        state,
        is_sort_by_date,
        is_sort_by_ascending,
        is_rub_transaction_only,
        filter_by_spec_word,
    )


def print_result(file_data: list[dict], file_type: str) -> None:
    """Выводит в консоль результат работы программы main()"""
    if file_data:
        print(f"Всего банковских операций в выборке: {len(file_data)}")
        for transaction in file_data:
            if transaction["description"] != "Открытие вклада":
                from_to_operation = (
                    f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}"
                )
            else:
                from_to_operation = f"{mask_account_card(transaction['to'])}"
            if file_type == "JSON":
                tr_time = datetime.strptime(transaction["date"], "%Y-%m-%dT%H:%M:%S.%f")
                print(tr_time.strftime("%d.%m.%Y"), transaction["description"])
                print(from_to_operation)
                print(
                    f"""
Сумма: {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['code']}\n"""
                )
            else:
                tr_time = datetime.strptime(transaction["date"], "%Y-%m-%dT%H:%M:%SZ")
                print(tr_time.strftime("%d.%m.%Y"), transaction["description"])
                print(from_to_operation)
                print(f"Сумма: {transaction['amount']} {transaction['currency_code']}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


def main() -> None:
    """Основная программа"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    (
        file_data,
        file_type,
        state,
        is_sort_by_date,
        is_sort_by_ascending,
        is_rub_transaction_only,
        filter_by_spec_word,
    ) = get_clarifications()

    file_data = filter_by_state(file_data, state)

    if is_sort_by_date:
        file_data = sort_by_date(file_data, is_sort_by_ascending)
    if is_rub_transaction_only:
        file_data = [data for data in filter_by_currency(file_data, "RUB")]
    if filter_by_spec_word != "False":
        file_data = filter_transactions_by_description(file_data, filter_by_spec_word)

    print("Распечатываю итоговый список транзакций...")
    print_result(file_data, file_type)


if __name__ == "__main__":
    main()




#     # src.widget / src.masks
#     print(mask_account_card("Maestro 1596837868705199"))
#     print(mask_account_card("MasterCard 7158300734726758"))
#     print(mask_account_card("Visa Classic 6831982476737658"))
#     print(mask_account_card("Visa Platinum 8990922113665229"))
#     print(mask_account_card("Visa Gold 5999414228426353"))
#
#     print(mask_account_card("Счет 64686473678894779589"))
#     print(mask_account_card("Счет 35383033474447895560"))
#     print(mask_account_card("Счет 73654108430135874305"))
#     print(get_time("2024-03-11T02:26:18.671407"))
#
#     # src.utils
#     transactions = get_data_from_json(PATH_TO_JSON_FILE)
#     for transaction in transactions:
#         print(get_amount_in_rubles(transaction))
#
#     # src.tabular_data
#     print(get_data_from_csv_file(PATH_TO_CSV_FILE))
#     print(get_data_from_excel_file(PATH_TO_XLSX_FILE))
#
#     # src.transaction_filtering
#     excel_data = get_data_from_excel_file(PATH_TO_XLSX_FILE)
#     print(filter_transactions_by_description(excel_data, 'Открытие вклада'))
#
#     category_list = ['Открытие вклада',
#                      'Перевод организации',
#                      "Перевод со счета на счет",
#                      "Перевод с карты на карту",
#                      ]
#     print(count_transactions_by_description(excel_data, category_list))
