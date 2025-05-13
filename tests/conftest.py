import pytest


@pytest.fixture
def card_number() -> str:
    return "7000792289606361"


@pytest.fixture
def account() -> str:
    return "73654108430135874305"


@pytest.fixture
def full_card_number1() -> str:
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def full_card_number2() -> str:
    return "Счет 64686473678894779589"


@pytest.fixture
def full_card_number3() -> str:
    return "Maestro 1596837868705199"


@pytest.fixture
def full_date1() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def full_date2() -> str:
    return "2025-05-13T15:26:18.671407"


@pytest.fixture
def my_list() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def my_list_for_day_sort() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def my_list_for_day_sort2() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2016-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2017-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2020-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
