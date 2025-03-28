import pytest

from src.widget import get_time, mask_account_card


@pytest.mark.parametrize(
    "card_info, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ],
)
def test_mask_account_card(card_info: str, expected: str) -> None:
    assert mask_account_card(card_info) == expected


def test_get_time(correct_time: str) -> None:
    assert get_time("2024-03-11T02:26:18.671407") == correct_time
