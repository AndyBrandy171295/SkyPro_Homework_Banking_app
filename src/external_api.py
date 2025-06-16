import json
import os
import requests
from dotenv import load_dotenv


load_dotenv()


with open("D:/PythonProjects/Banking_app/data/operations.json", encoding="utf-8") as json_file:
    transaction = json.load(json_file)


class CurrencyConversionError(Exception):
    pass


class InvalidAPIKey(Exception):
    pass


def sum_transactions(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    тип данных — float"""
    amount = float(transaction.get("amount", 0))
    currency = transaction.get("currency", "").upper()

    if currency == "RUB":
        return amount

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise InvalidAPIKey("Неверный ключ API")

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"
    headers = {"apikey": api_key}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()

        if "rates" not in data or "RUB" not in data["rates"]:
            raise CurrencyConversionError("Invalid API response format")

        rub_rate = data["rates"]["RUB"]

        return amount * rub_rate

    except requests.RequestException as e:
        print(f"Произошла ошибка {e}, повторите запрос позже!")

    except (ValueError, KeyError) as e:
        print(f"Ошибка данных {e} в транзакции!")
