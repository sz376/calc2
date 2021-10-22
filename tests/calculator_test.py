"""Testing the Calculator"""
from calculator.main import Calculator


def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0


def test_calculator_add():
    """Testing the Add function of the calculator"""
    # Arrange by instantiating the calc class
    calc = Calculator()
    # Act by calling the method to be tested
    calc.add_number(1)
    # Assert that the results are correct
    assert calc.result == 1


def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    calc.add_number(1)
    assert calc.get_result() == 1


def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.get_result() == -1


def test_calculator_multiply():
    """Testing the subtract method of the calculator
    Note that 2 is added to result first to get a product != 0"""
    calc = Calculator()
    calc.add_number(2)
    calc.multiply_number(3)
    assert calc.get_result() == 6


def test_calculator_divide():
    """Testing the subtract method of the calculator
    Note that 6 is added to result first to avoid dividing by zero"""
    calc = Calculator()
    calc.add_number(6)
    calc.divide_number(3)
    assert calc.get_result() == 2

def test_calculator_divide_by_zero():
    """Testing the division method of the calculator
    divisionbyzero error catching"""
    calc = Calculator()
    calc.add_number(6)
    assert calc.divide_number(0) == "You can't divide by zero!"
