def filter_by_currency(list_of_dicts: list, currency: str) -> list:
    """Программа принимает список словарей и возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)"""
    for dict in list_of_dicts:
        if dict["operationAmount"]["currency"]["code"] == currency:
            yield dict


def transaction_descriptions(list_of_dicts: list) -> str:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    yield from (dict["description"] for dict in list_of_dicts)


def card_number_generator(start, stop) -> str:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    card_mask = "0000000000000000"
    for card in range(start, stop + 1):
        if len(str(card)) >= 17:
            yield f"Неверные данные!"
        card_mask = card_mask[: -len(str(card))] + str(card)
        yield f"{card_mask[:4]} {card_mask[4:8]} {card_mask[8:12]} {card_mask[12:]}"
