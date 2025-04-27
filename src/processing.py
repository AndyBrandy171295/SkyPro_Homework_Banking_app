def filter_by_state(list_of_dict: [list], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает список словарей и возвращает новый,
    содержащий только те словари, у которых ключ state соответствует указанному значению"""
    new_filtered_list = []
    for dict in list_of_dict:
        if dict["state"] == state:
            new_filtered_list.append(dict)
    return new_filtered_list



