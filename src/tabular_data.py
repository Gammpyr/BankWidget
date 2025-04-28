import pandas as pd


def get_data_from_csv_file(file_path: str) -> list[dict]:
    """Принимает путь к CSV файлу и возвращает список словарей из него"""
    csv_data = pd.read_csv(file_path, delimiter=";")

    return csv_data.to_dict(orient="records")


def get_data_from_excel_file(file_path: str) -> list[dict]:
    """Принимает путь к Excel файлу и возвращает список словарей из него"""
    csv_data = pd.read_excel(file_path)

    return csv_data.to_dict(orient="records")


# Вариант №2 для CSV
# def get_data_from_csv_file(file_path: str) -> list[dict]:
#     """Принимает путь к CSV файлу и возвращает список со словарями из него"""
#
#     with open(file_path, encoding='utf-8') as file:
#         data = csv.DictReader(file, delimiter=';')
#         return list(data)
