from functools import wraps


def log(filename=None):
    """Декоратор-логгер, который записывает лог либо в файл, либо выводит на экран."""
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                log_message = f"Вызов функции {function.__name__} с аргументами {args} и {kwargs}"
            except Exception as e:
                error_type = type(e).__name__
            log_message = f"{function.__name__}: {error_type}. С аргументами {args} и {kwargs}"
            result = None
            if filename:
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(log_message + '\n')
            else:
                print(log_message)
                return result

        return wrapper
    return decorator

