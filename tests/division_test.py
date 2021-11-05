"""Testing Division"""
from calc.calculations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for division"""
    #Arrange
    mynumbers = (1.0,2.0)
    division = Division(mynumbers)
    #Act
    #Assert
    assert division.get_result() == 0.5

def test_calculation_division_by_zero():
    """testing that our calculator has a proper response for division by zero"""
    mynumbers = (0.0, 0.0)
    division = Division(mynumbers)
    # Act
    # Assert
    assert division.get_result() == "You can't divide by zero!"
