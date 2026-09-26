import subprocess
import sys

import pytest

from calculator import add, subtract, multiply, divide, power, calculate


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_power():
    assert power(2, 3) == 8


def test_power_with_negative_exponent():
    assert power(2, -1) == 0.5


def test_calculate_dispatches_to_operation():
    assert calculate("add", 1, 2) == 3
    assert calculate("mul", 2, 3) == 6
    assert calculate("pow", 2, 3) == 8


def test_calculate_unknown_operation():
    with pytest.raises(ValueError):
        calculate("mod", 1, 2)


def test_cli_add():
    result = subprocess.run(
        [sys.executable, "calculator.py", "add", "2", "3"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "5.0"


def test_cli_pow():
    result = subprocess.run(
        [sys.executable, "calculator.py", "pow", "2", "3"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "8.0"


def test_cli_divide_by_zero_exits_with_error():
    result = subprocess.run(
        [sys.executable, "calculator.py", "div", "1", "0"],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "division by zero" in result.stderr
