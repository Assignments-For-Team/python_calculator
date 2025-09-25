# test_python_calculator.py

from python_calculator import subtract_numbers

# 1. Positive numbers
def test_subtract_positive_numbers():
    assert subtract_numbers(10, 5) == 5

# 2. Negative result
def test_subtract_negative_result():
    assert subtract_numbers(5, 10) == -5

# 3. Zero involved
def test_subtract_with_zero():
    assert subtract_numbers(7, 0) == 7
    assert subtract_numbers(0, 7) == -7

# 4. Negative numbers
def test_subtract_negative_numbers():
    assert subtract_numbers(-3, -2) == -1
    assert subtract_numbers(-5, 3) == -8

# 5. Subtracting the same number
def test_subtract_same_numbers():
    assert subtract_numbers(7, 7) == 0
    assert subtract_numbers(-4, -4) == 0

# 6. Floating-point numbers
def test_subtract_floats():
    assert subtract_numbers(5.5, 2.2) == 3.3
    assert subtract_numbers(-1.1, -2.2) == 1.1
