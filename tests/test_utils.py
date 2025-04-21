import json
from typing import Any
from unittest.mock import mock_open, patch

from src.utils import get_amount_in_rubles, get_data_from_json

json_file = [
    {
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
    }
]


@patch("builtins.open", new_callable=mock_open, read_data=json.dumps(json_file))
def test_get_data_from_json(mock_open: Any) -> None:
    result = get_data_from_json("fake_file.json")

    assert result == json_file


@patch("builtins.open", new_callable=mock_open, read_data='{"date": "2025-04-21", "info": {"rate": 3.0}}')
def test_get_amount_in_rubles(mock_file: Any) -> None:
    test_json_file = {"operationAmount": {"currency": {"code": "USD"}, "amount": "2.0"}}
    result = get_amount_in_rubles(test_json_file)
    assert result == 6.0
