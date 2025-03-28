from src.masks import get_mask_account, get_mask_card_number


def test_mask_card() -> None:
    assert get_mask_card_number("1596837868705199") == "1596 83** **** 5199"


def test_mask_account() -> None:
    assert get_mask_account("64686473678894779589") == "**9589"
