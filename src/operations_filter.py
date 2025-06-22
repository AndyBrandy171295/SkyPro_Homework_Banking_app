import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""
    results = []
    for i in data:
        if re.search(search, i.get("description", ""), re.IGNORECASE):
            results.append(i)
    return results


def process_bank_operation(data: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это кол-во операций в каждой категории."""

    category_counts = {category: 0 for category in categories}

    for operation in data:
        description = operation.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1

        return category_counts


if __name__ == "__main__":
    qwer = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    qwer1 = ["Перевод"]

    # print(process_bank_search(qwer, 'Перевод'))
    print(process_bank_operation(qwer, qwer1))
