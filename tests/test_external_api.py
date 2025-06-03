from unittest.mock import Mock, patch, ANY
from src.external_api import sum_transactions
import requests
import pytest


@patch('requests.get')
def test_sum_transactions(mock_get, one_transaction):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 757861.896388}

    assert sum_transactions(one_transaction) == 757861.896388

    mock_get.assert_called_once_with(
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={one_transaction[0]['operationAmount']['currency']['code']}&amount={one_transaction[0]['operationAmount']['amount']}",
        headers=ANY
    )