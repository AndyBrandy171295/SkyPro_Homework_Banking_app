import pytest
from src.operations_filter import process_bank_search, process_bank_operation


def test_process_bank_search(transactions):
    result = [{'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
               'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
               'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
               'to': 'Счет 75651667383060284188'},
              {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
               'operationAmount': {'amount': '43318.34',
                                   'currency': {'name': 'руб.', 'code': 'RUB'}},
               'description': 'Перевод со счета на счет',
               'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'}]

    assert process_bank_search(transactions, 'счет') == result

def test_process_bank_search_empty(transactions):
    result = []

    assert process_bank_search(transactions, 'авангард') == result


def test_process_bank_operation(transactions):
    result = {}

    assert process_bank_operation(transactions, ['счет']) == result

def test_process_bank_operation_2_value(transactions):
    result = {'Перевод': 1}

    assert process_bank_operation(transactions, ['счет', 'Перевод']) == result

def test_process_bank_operation_empty(transactions):
    result =  {}

    assert process_bank_operation(transactions, []) == result