import json
from unittest.mock import patch, mock_open


from src.utils import get_data_from_json, get_amount_in_rubles
from src.external_api import convert_to_rub

json_file = [
    {
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            },
        },
    }
]


@patch('builtins.open', new_callable=mock_open, read_data=json.dumps(json_file))
def test_get_data_from_json(mock_open):
    result = get_data_from_json('fake_file.json')

    assert result == json_file


