import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')

with open("D:/PythonProjects/Banking_app/data/operations.json", encoding="utf-8") as json_file:
    transaction = json.load(json_file)


def sum_transactions(transaction: dict) -> float:
    '''Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float'''
    headers = {"apikey": API_KEY}
    total_sum = 0.0

    for i in transaction:
        if i == {}:
            print('Пустое значение!')
        else:
            amount = float(i["operationAmount"]["amount"])
            to = 'RUB'
            from_usd = 'USD'
            from_eur = 'EUR'

            if i["operationAmount"]["currency"]["code"] == 'RUB':
                total_sum += amount

            elif i["operationAmount"]["currency"]["code"] == 'USD':
                response = requests.get(
                    f'https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_usd}&amount={amount}',
                    headers=headers
                )
                if response.status_code == 200:
                    data_usd = response.json()
                    total_sum += float(data_usd["result"])
                else:
                    print("Ошибка запроса к API:", response.status_code)

            elif i["operationAmount"]["currency"]["code"] == 'EUR':
                response = requests.get(
                    f'https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_eur}&amount={amount}',
                    headers=headers
                )
                if response.status_code == 200:
                    data_eur = response.json()
                    total_sum += float(data_eur["result"])
                else:
                    print("Ошибка запроса к API:", response.status_code)

    return total_sum

qwer = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


print(sum_transactions(qwer))
