from src.widget import get_date, get_mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 64686473678894779589", "Счет 6473 67** **** 9589"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ],
)
def test_get_mask_account_card(value: str, expected: str) -> str:
    assert get_mask_account_card(value) == expected


def test_get_date(full_date1: str) -> None:
    assert get_date(full_date1) == "11.03.2024"

    assert get_date(full_date2) == "13.05.2025"
