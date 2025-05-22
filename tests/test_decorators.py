import pytest


def example(num1, num2):
    if num1 or num2 <= 0:
        raise ValueError("Все аргументы должны быть положительными!")
    return num1 + num2


def test_log(capsys):
    with pytest.raises(ValueError, match="Все аргументы должны быть положительными!"):
        example(-1, 2)