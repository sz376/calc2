"""controls the calculator page"""
import time
from flask import render_template, request, flash
from app.controllers.controller import ControllerBase # pylint: disable=no-name-in-module, import-error
from calc.calculator import Calculator
from csvcalc.csvwriter import CSVwriter
from csvcalc.csvreader import CSVreader

class CalculatorController(ControllerBase):
    """class for handling a page"""

    @staticmethod
    def post():
        """main method"""
        if request.form["value1"] == "" or request.form["value2"] == "":
            error = "You must enter a value for value 1 and or value 2"
        else:
            flash("You successfully calculated")
            # get the values out of the form
            value1 = request.form["value1"]
            value2 = request.form["value2"]
            operation = request.form["operation"]
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            if operation == "division":
                if value2 == 0:
                    result = "Division by Zero"
                else:
                    Calculator.division(my_tuple)
                    result = Calculator.get_last_result_value()
            elif operation == "addition":
                Calculator.addition(my_tuple)
                result = Calculator.get_last_result_value()
            elif operation == "subtraction":
                Calculator.subtraction(my_tuple)
                result = Calculator.get_last_result_value()
            elif operation == "multiplication":
                Calculator.multiplication(my_tuple)
                result = Calculator.get_last_result_value()
            CSVwriter.write_log(time.time(), operation, value1, value2, result)
            data = CSVreader.csv_to_json()
            return render_template(
                "result.html",
                value1=value1,
                value2=value2,
                operation=operation,
                result=result,
                data=data,
            )
        return render_template("calculator.html", error=error)

    @staticmethod
    def get():
        """return the calculator"""
        return render_template("calculator.html")
