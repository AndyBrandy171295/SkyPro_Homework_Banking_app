import json


def json_operation(json_path: str) -> list:
    '''Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях'''
    try:
        with open(json_path, encoding='utf-8') as j_file:
            data = json.load(j_file)
            print("Файл успешно прочитан, данные:", data)
        return data
    except json.JSONDecodeError:
        print('Ошибка чтения файла!')
        return []
    except FileNotFoundError:
        print('Файл не найден!')
        return []


if __name__ == '__mane__':
    result = json_operation('data/operations.json')
    print(result)

