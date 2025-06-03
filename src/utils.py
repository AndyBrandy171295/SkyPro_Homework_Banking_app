import json
import logging


logging.basicConfig(level=logging.DEBUG,
                    format='%(acstime)s - %(name)s - %(levelname)s: %(message)s',
                    filename='D:/PythonProjects/Banking_app/logs/utils.log',
                    filemode='w',
                    encoding='utf-8')

utils_logger = logging.getLogger('json_operation')

def json_operation(json_path: str) -> list:
    '''Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях'''
    try:
        utils_logger.info('Открываю json-файл.')
        with open(json_path, encoding='utf-8') as j_file:
            data = json.load(j_file)
            utils_logger.info(f"Файл успешно прочитан, данные: {data}")
        return data
    except json.JSONDecodeError:
        utils_logger.error('Ошибка чтения файла!')
        return []
    except FileNotFoundError:
        utils_logger.error('Файл не найден!')
        return []
