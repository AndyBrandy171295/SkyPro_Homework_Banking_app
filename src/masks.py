def get_mask_card_number(card_number: str) -> str:
    """Функция показывает маску карты"""
    if len(card_number) == 16:
        mask_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return mask_card
    return 'Неверный номер карты'


def get_mask_account(account_number: str) -> str:
    """Функция показывает маску счета"""
    mask_account = f"**{account_number[-4:]}"
    return mask_account
