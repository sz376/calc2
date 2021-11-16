""" This is the main flask driver"""
import flask
import calc.calculator

app = flask.Flask(__name__)

@app.route('/')
def hello():
    """greeting page"""
    return flask.render_template('calculator.html')


@app.route("/calculator", methods=["POST"])
def calculate():
    """calculation operation on received values"""
    values = flask.request.form["values"]
    values = tuple(map(int, values.split(',')))
    operation = flask.request.form["operation"]

    if operation == "add":
        calc.calculator.Calculator.add_numbers(values)
        result = calc.calculator.Calculator.get_result_value()
        return flask.render_template("calculator.html", result=result)
    if operation == "subtract":
        calc.calculator.Calculator.subtract_numbers(values)
        result = calc.calculator.Calculator.get_result_value()
        return flask.render_template("calculator.html", result=result)
    if operation == "multiply":
        calc.calculator.Calculator.subtract_numbers(values)
        result = calc.calculator.Calculator.get_result_value()
        return flask.render_template("calculator.html", result=result)
    if operation == "divide":
        calc.calculator.Calculator.subtract_numbers(values)
        result = calc.calculator.Calculator.get_result_value()
        return flask.render_template("calculator.html", result=result)

    return flask.render_template("calculator.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
