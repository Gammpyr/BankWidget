from typing import Any
from unittest.mock import patch

import pandas as pd

from src.tabular_data import get_data_from_csv_file, get_data_from_excel_file

df = pd.DataFrame({"name": ["Sasha", "Iiiigor"], "age": ["15", "60"]})


@patch("pandas.read_csv")
def test_get_data_from_csv_file(mock_read: Any) -> None:
    mock_read.return_value = df

    result = get_data_from_csv_file("fake_file.csv")

    assert result == [{"age": "15", "name": "Sasha"}, {"age": "60", "name": "Iiiigor"}]


@patch("pandas.read_excel")
def test_get_data_from_excel_file(mock_read: Any) -> None:
    mock_read.return_value = df

    result = get_data_from_excel_file("fake_file.xlsx")

    assert result == [{"age": "15", "name": "Sasha"}, {"age": "60", "name": "Iiiigor"}]
