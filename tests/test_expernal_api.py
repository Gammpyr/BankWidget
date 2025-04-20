from unittest.mock import patch

import pytest

from src.external_api import convert_to_rub


@patch('requests.get')
def test_convert_to_rub(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "query": {
            "from": "USD",
            "amount": 1
        },
        "info": {
            "rate": 2
        },
        "date": "2000-01-01",
        "result": 3.3
    }

    result = convert_to_rub('USD', 2)
    assert result == 3.3

@patch('requests.get')
def test_convert_to_rub_no_currency(mock_get):
    mock_get.return_value.status_code = 800
    mock_get.return_value.json.return_value = {
        "query": {
            "from": "USD",
            "amount": 1
        },
        "info": {
            "rate": 2
        },
        "date": "2000-01-01",
        "result": 3.3
    }

    with pytest.raises(ValueError, match="Failed to get currency rate. Status code: 800"):
        convert_to_rub('USD', 2)


