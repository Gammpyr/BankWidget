import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
ERD_API_KEY = os.getenv("ERD_API_KEY")
headers = {"apikey": ERD_API_KEY}


def convert_to_rub(_from: str, amount: float) -> Any:
    """
    Принимает код валюты и сумму.
    Возвращает сумму, конвертированную в указанную валюту.
    """
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={_from}&amount={amount}"
    response = requests.get(url, headers=headers)
    status_code = response.status_code

    if status_code != 200:
        raise ValueError(f"Failed to get currency rate. Status code: {status_code}")

    response_data = response.json()

    with open(f"../data/{_from}.json", "w", encoding="utf-8") as f:
        json.dump(response_data, f, indent=4)

    return response_data["result"]
