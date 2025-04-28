# Bank Widget

![SkyPro](https://res.cloudinary.com/admitad-gmbh/image/upload/f_auto,h_0.5/v1671725214/x9o5qcorfliychngyjpk.webp)

## Описание:
Виджет для банка, разрабатываемый во время обучения языку Python.

## Содержание

- [Основные функции](#основные-функции-на-данный-момент )
- [Установка](#установка)
- [Тестирование](#тестирование)


## Основные функции, на данный момент:


[config.py](src/config.py)
- Содержит информацию о путях к файлам

[decorators.py](src/decorators.py)
1. `log` - Регистрирует детали выполнения функций и сохраняет их в файл (если его имя указано)

[external_api.py](src/external_api.py)
1. Принимает код валюты и сумму и возвращает сумму, конвертированную в указанную валюту.

[generators.py](src/generators.py)
1. `filter_by_currency` - возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной
2. `transaction_descriptions` - Принимает список словарей с транзакциями и возвращает описание каждой операции, 
    по очереди
3. `card_number_generator` - выдает номера банковских карт в формате XXXX XXXX XXXX XXXX

[masks.py](src/masks.py)
1. `get_mask_card_number` - Принимает номер карты и возвращает его маску
2. `get_mask_account` - Принимает номер счета и возвращает маску формата **XXXX

[processing.py](src/processing.py)
1. `filter_by_state` - возвращает новый список словарей,
    у которых ключ state соответствует указанному значению
2. `sort_by_date` - Возвращает новый список, отсортированный по дате

[tabular_data.py](src/tabular_data.py)
1. `get_data_from_csv_file` - Принимает путь к CSV файлу и возвращает список словарей из него
2. `get_data_from_excel_file` - Принимает путь к Excel файлу и возвращает список словарей из него

[utils.py](src/utils.py)
1. `get_data_from_json` - Получает путь к файлу json и возвращает словарь с данными
2. `get_amount_in_rubles` - Получает словарь с транзакцией и возвращает сумму транзакции

[widget.py](src/widget.py)
1. `mask_account_card` - Определяет тип карты/счёта и возвращает соответствующую маску
2. `get_time` - Получает время и возвращает в формате ДД.ММ.ГГГГ






## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/Gammpyr/BankWidget_10.1.git
```
2. Установите Poetry
```
pip install poetry

poetry init
```
3. Установите зависимости:
```
poetry install
```

## Тестирование
В проекте используется фреймворк Pytest. Для установки и запуска выполните команды:
```
poetry add --group dev pytest
```
```
poetry run pytest
```
