from src.databases_reader import read_transaction_from_xlsx, read_transactions_from_csv
from src.masks import get_mask_account, get_mask_card_number
from src.operations_filter import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.utils import json_operation


JSON_PATH = r"D:\PythonProjects\Banking_app\data\operations.json"
CSV_PATH = r"D:\PythonProjects\Banking_app\databases\transactions.csv"
XLSX_PATH = r"D:\PythonProjects\Banking_app\databases\transactions_excel.xlsx"


def load_transaction(file_path: str) -> list[dict]:
    """Загрузка транзакций в зависимости от типа файла"""
    if file_path.endswith(".json"):
        return json_operation(file_path)
    elif file_path.endswith(".csv"):
        return read_transactions_from_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return read_transaction_from_xlsx(file_path)
    else:
        []


def make_choice() -> str:
    """Функция дает пользователю выбор формата чтения данных"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями. ")

    json_choice = "1. Получить информацию о транзакциях из JSON-файла"
    csv_choice = "2. Получить информацию о транзакциях из CSV-файла"
    xlsx_choice = "3. Получить информацию о транзакциях из XLSX-файла"

    while True:
        user_choice = input(f"Выберите необходимый пункт меню: \n{json_choice}\n{csv_choice}\n{xlsx_choice}").strip()

        if user_choice == "1":
            print("Для обработки выбран JSON-файл.")
            return JSON_PATH

        elif user_choice == "2":
            print("Для обработки выбран CSV-файл.")
            return CSV_PATH

        elif user_choice == "3":
            print("Для обработки выбран XLSX-файл.")
            return XLSX_PATH

        else:
            print("Ошибка ввода, введите цифру варианта из списка.")


def get_status_filter() -> str:
    """Получение статуса для фильтрации от пользователя"""
    user_choice = input("""Введите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""").upper()

    if user_choice in ["EXECUTED", "CANCELED", "PENDING"]:
        return user_choice
    else:
        print(f'Статус операции "{user_choice}" недоступен."')
        return get_status_filter()


def apply_additional_filters(transactions: list[dict]) -> list[dict]:
    """Применение дополнительных фильтров по выбору пользователя"""
    if input("Отсортировать операции по дате? Да/Нет").lower() == "да":
        transactions = sort_by_date(transactions)
        if input("Отсортировать по возрастанию или по убыванию?"):
            transactions = sort_by_date(transactions, reverse=True)

    if input("Выводить только рублевые транзакции? Да/Нет").lower == "да":
        transactions = filter_by_state(transactions, "RUB")

    if input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").lower() == "да":
        special_word = input("Введите слово: ")
        transactions = process_bank_search(transactions, special_word)

    return transactions


def print_transaction(transactions: list[dict]):
    """Печать отфильтрованных транзакций"""
    print("\nРаспечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transactions)}\n")

    if not transactions:
        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"

    for transaction in transactions:
        date = transaction.get("date", "")
        description = transaction.get("description", "")
        from_ = transaction.get("from", "")
        to_ = transaction.get("to", "")
        amount = transaction.get("amount", "")
        currency = transaction.get("currency", "")
        if "Счет" in from_:
            from_ = get_mask_account(from_)
        else:
            from_ = get_mask_card_number(from_)

        if "Счет" in to_:
            to_ = get_mask_account(to_)
        else:
            to_ = get_mask_card_number(to_)

        print(f"{date} {description}")
        if from_:
            print(f"{from_} -> ", end="")
        print(f"{to_}")
        print(f"Сумма: {amount} {currency}\n")


def main():
    """Основная функция программы"""
    try:
        file_path = make_choice()

        transactions = load_transaction(file_path)

        status = get_status_filter()
        filtered = filter_by_state(transactions, status)

        filtered = apply_additional_filters(filtered)
        print_transaction(filtered)
    except Exception as e:
        print(f"Произошла ошибка {e}")


if __name__ == "__main__":
    main()
