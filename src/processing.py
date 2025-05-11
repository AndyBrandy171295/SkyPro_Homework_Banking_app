def filter_by_state(list_of_dict: [list], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает список словарей и возвращает новый,
    содержащий только те словари, у которых ключ state соответствует указанному значению"""
    new_filtered_list = []
    for dict in list_of_dict:
        if dict["state"] == state:
            new_filtered_list.append(dict)
    return new_filtered_list


def sort_by_date(list_of_dicts: [list], reverse: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей и возвращает новый, отсортированный по дате"""
    return sorted(list_of_dicts, key=lambda x: x["date"], reverse=True)
