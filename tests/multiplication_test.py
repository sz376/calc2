"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication

def test_calculation_multiplication():
    """testing that our calculator has a static method for multiplication"""
    mynumbers = (1.0,2.0)
    multiplication = Multiplication(mynumbers)
    assert multiplication.get_result() == 2.0
