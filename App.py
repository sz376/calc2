from flask import render_template, request
from keep_alive import keep_alive, app
import calc.calculator


@app.route("/")
def main():
    return render_template("calculator.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    values = request.form["values"]
    values = tuple(map(int, values.split(',')))
    operation = request.form["operation"]

    if operation == "add":
        calc.calculator.Calculator.add_numbers(values)
        result = calc.calculator.Calculator.get_result_value()
        return render_template("calculator.html", result=result)

    elif operation == "subtract":
        calc.calculator.Calculator.subtract_numbers(values)
        result = calc.calculator.Calculator.get_result_value()
        return render_template("calculator.html", result=result)

    elif operation == "multiply":
        calc.calculator.Calculator.subtract_numbers(values)
        result = calc.calculator.Calculator.get_result_value()
        return render_template("calculator.html", result=result)

    elif operation == "divide":
        calc.calculator.Calculator.subtract_numbers(values)
        result = calc.calculator.Calculator.get_result_value()
        return render_template("calculator.html", result=result)

    else:
        return render_template("calculator.html")

if __name__ == "__main__":
    keep_alive()
