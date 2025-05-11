from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number: str) -> None:
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"

    assert get_mask_card_number("12344") == "Неверный номер карты"


def test_get_mask_account(account: str) -> None:
    assert get_mask_account(account) == "**4305"
