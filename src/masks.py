def get_mask_card_number(card_number: str) -> str:
    """Функция показывает маску счета"""
    mask_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return mask_card


def get_mask_account(account_number: str) -> str:
    """Функция показывает маску счета"""
    mask_account = f"**{account_number[-4:]}"
    return mask_account
