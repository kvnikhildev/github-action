# test_calculator.py

import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract():
    assert calculator.subtract(5, 2) == 3
    assert calculator.subtract(0, 5) == -5
    assert calculator.subtract(3, 3) == 0

def test_multiply():
    assert calculator.multiply(4, 2) == 8
    assert calculator.multiply(0, 10) == 0
    assert calculator.multiply(-2, 3) == -6
