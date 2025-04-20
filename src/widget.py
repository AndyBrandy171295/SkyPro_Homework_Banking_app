def get_mask_account_card(card_number: str) -> str:
    """Функция для маскировки номера карты"""
    alpha_part_of_mask_card = ""
    for char in card_number:
        if char.isalpha() or char == " ":
            alpha_part_of_mask_card += char
    return f"{alpha_part_of_mask_card}{card_number[-16:-11]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def get_date(full_date: str) -> str:
    """Функция для, которая определяет дату в формате ДД.ММ.ГГГГ"""
    return f"{full_date[8:10]}.{full_date[5:7]}.{full_date[:4]}"
