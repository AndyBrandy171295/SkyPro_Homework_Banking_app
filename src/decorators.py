from functools import wraps


def log(filename=None):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print(f"Функция {function.__name__} начала работу.")
            result = function(*args, **kwargs)
            for i in args:
                if i <= 0:
                    raise ValueError("Все аргументы должны быть положительными!")
            for i in kwargs:
                if i <= 0:
                    raise ValueError("Все аргументы должны быть положительными!")
            print(f"Функция {function.__name__} вывела результат.")
            print(f"Функция {function.__name__} закончила работу.")
            return result

        return wrapper

    return decorator

