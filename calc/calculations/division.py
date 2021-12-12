"""Multiplication Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        if self.values[1] == 0:
            return "Zero division error"
        else:
            return self.values[0] / self.values[1]
