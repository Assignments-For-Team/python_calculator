# test_python_calculator.py
import pytest

from python_calculator import add_numbers

# --- Addition tests ---

# 1. Positive numbers
def test_add_positive_numbers():
    assert add_numbers(5, 3) == 8
    assert add_numbers(10, 7) == 17

# 2. Negative numbers
def test_add_negative_numbers():
    assert add_numbers(-5, -3) == -8
    assert add_numbers(-5, 3) == -2
    assert add_numbers(5, -3) == 2

# 3. Zero involved
def test_add_with_zero():
    assert add_numbers(0, 5) == 5
    assert add_numbers(5, 0) == 5
    assert add_numbers(0, 0) == 0

# 4. Same numbers
def test_add_same_numbers():
    assert add_numbers(7, 7) == 14
    assert add_numbers(-4, -4) == -8

# 5. Floating-point numbers
def test_add_floats():
    assert add_numbers(2.5, 3.1) == pytest.approx(5.6)
    assert add_numbers(-1.1, -2.2) == pytest.approx(-3.3)

# 6. Mixed numbers
def test_add_mixed_numbers():
    assert add_numbers(5, -2) == 3
    assert add_numbers(-3, 7) == 4

#--------------------------------------------------

# --- Subtraction tests ---

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

#---------------------------------------------------

# --- Division tests ---

from python_calculator import divide_numbers  

def test_divide_normal():
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(9, 3) == 3
    assert divide_numbers(-8, 2) == -4

def test_divide_with_floats():
    assert divide_numbers(7, 2) == 3.5
    assert divide_numbers(5.5, 2.2) == pytest.approx(2.5, rel=1e-2)

def test_divide_by_zero():
    assert divide_numbers(10, 0) == "Error: Division by zero!"

