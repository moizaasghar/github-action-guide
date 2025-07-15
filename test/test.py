import pytest
from src.calculator import calculator

@pytest.fixture
def calc():
    return calculator()

def test_add(calc):
    assert calc.add(5, 3) == 8

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2

def test_multiply(calc):
    assert calc.multiply(5, 3) == 15

def test_divide_by_zero(calc):
    assert calc.divide(5, 0) == "Division by zero error"
