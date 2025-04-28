from src.config import PATH_TO_CSV_FILE, PATH_TO_JSON_FILE, PATH_TO_XLSX_FILE
from src.tabular_data import get_data_from_csv_file, get_data_from_excel_file
from src.utils import get_amount_in_rubles, get_data_from_json
from src.widget import get_time, mask_account_card

if __name__ == "__main__":
    # src.widget / src.masks
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))

    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_time("2024-03-11T02:26:18.671407"))

    # src.utils
    transactions = get_data_from_json(PATH_TO_JSON_FILE)
    for transaction in transactions:
        print(get_amount_in_rubles(transaction))

    # src.tabular_data
    print(get_data_from_csv_file(PATH_TO_CSV_FILE))
    print(get_data_from_excel_file(PATH_TO_XLSX_FILE))
