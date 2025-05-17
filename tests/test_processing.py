from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(my_list):
    assert filter_by_state(my_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date(my_list_for_day_sort: list) -> list:
    assert sort_by_date(my_list_for_day_sort) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date2(my_list_for_day_sort2: list) -> list:
    assert sort_by_date(my_list_for_day_sort2) == [
        {"id": 594226727, "state": "CANCELED", "date": "2020-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2017-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2016-07-03T18:35:29.512364"},
    ]
