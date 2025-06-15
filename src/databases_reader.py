import pandas as pd
import csv
from typing import List, Dict


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    '''Функция для считывания финансовых операций из CSV принимает путь к файлу CSV в качестве аргумента.'''
    transactions = []
    try:
        if not file_path.endswith('.csv'):
            raise ValueError('Неподдерживаемый формат файла. Используйте .csv')
        with open(file_path, encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')

            for row in reader:
                transaction = {
                    'id': row.get('id'),
                    'state': row.get('state'),
                    'date': row.get('date'),
                    'amount': row.get('amount'),
                    'currency_name': row.get('currency_name'),
                    'currency_code': row.get('currency_code'),
                    'from': row.get('from'),
                    'to': row.get('to'),
                    'description': row.get('description')
                }
                transactions.append(transaction)
        return transactions
    except FileNotFoundError:
        print(f'Файл не найден {file_path}')
        return []
    except Exception as e:
        print(f'Ошибка чтения файла {e}')
        return []


def read_transaction_from_xlsx(file_path: str) -> List[Dict]:
    '''Функция для считывания финансовых операций из XLSX принимает путь к файлу XLSX в качестве аргумента.'''
    transactions = []
    try:
        if not file_path.endswith('.xlsx'):
            raise ValueError('Неподдерживаемый формат файла. Используйте .xlsx')
        df = pd.read_excel(file_path, dtype=str, engine='openpyxl')
        transactions = df.to_dict(orient="records")
        return transactions
    except FileNotFoundError:
        print(f'Файл не найден {file_path}')
        return []
    except Exception as e:
        print(f'Ошибка чтения файла {e}')
        return []


if __name__=='__main__':
    print(read_transactions_from_csv('D:/PythonProjects/Banking_app/databases/transactions.csv'))
    # print(read_transaction_from_xlsx('D:/PythonProjects/Banking_ap/databases/transactions_excel.xlsx'))