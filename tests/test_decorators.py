import pytest

from src.decorators import log


@log
def add(a, b):
    return a + b


@log(filename='test_log.txt')
def multiply(a, b):
    return a * b

@log(None)
def test_add_log(capsys):
    result = add(3, 4)
    assert result == 7
    captured = capsys.readouterr().out
    assert 'Вызов функции add с аргументами (3, 4) и {} - результат: 7' in captured.out


@log(filename='test_log.txt')
def test_multiply_log():
    result = multiply(3, 4)
    assert result == 12
    with open('test_log.txt', 'r', encoding='utf-8') as f:
        read_file = f.read()
    assert 'Вызов функции multiply с аргументами (3, 4) и {} - результат: 12' in read_file
