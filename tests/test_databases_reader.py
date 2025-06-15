import pytest
from unittest.mock import Mock, patch, mock_open
from src.databases_reader import read_transaction_from_xlsx, read_transactions_from_csv
import pandas as pd
import os
import csv


@patch('builtins.open', new_callable=mock_open)
@patch('pandas.read_excel')
def test_empty_read_transactions_from_xlsx(mock_read_excel, mock_open):
    mock_read_excel.return_value = pd.DataFrame()
    result = read_transaction_from_xlsx('transactions_excel.xlsx')

    assert result == []
    mock_open.assert_not_called()
    mock_read_excel.assert_called_once_with(
        'transactions_excel.xlsx',
        dtype=str,
        engine='openpyxl'
    )


@patch('builtins.open', new_callable=mock_open)
def test_read_from_xlsx_file_not_found(open_mock):
    mock_open.side_effect = FileNotFoundError('Файл не найден D:/PythonProjects/Banking_app/databases/transactions_excel.xlsx')
    result = read_transaction_from_xlsx('file.xlsx')

    assert result == []


@patch('builtins.open', new_callable=mock_open, read_data='''id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации
''')
def test_read_transaction_from_csv(mock_open):
    expected = [{'id': '650703',
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': '16210',
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'}]

    result = read_transactions_from_csv(os.path.abspath('transactions.csv'))

    assert result == expected
    mock_open.assert_called_once_with(
        os.path.abspath('transactions.csv'),
        encoding='utf-8'
    )
