"""Multiplication Class"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the multiplication results"""
        return self.values[0] * self.values[1]
