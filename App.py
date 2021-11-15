import os
import flask
import calc.calculator


app = flask.Flask(__name__)

@app.route('/')
def hello():
    return flask.render_template('calculator.html')
    
@app.route("/calculate", methods=["POST"])
def calculate():
    values = flask.request.form["values"]
    values = tuple(map(int, values.split(',')))
    operation = flask.request.form["operation"]

    if operation == "add":
        calc.calculator.Calculator.add_numbers(values)
        result = calc.calculator.Calculator.get_result_value()
        return flask.render_template("calculator.html", result=result)

    elif operation == "subtract":
        calc.calculator.Calculator.subtract_numbers(values)
        result = calc.calculator.Calculator.get_result_value()
        return flask.render_template("calculator.html", result=result)

    elif operation == "multiply":
        calc.calculator.Calculator.subtract_numbers(values)
        result = calc.calculator.Calculator.get_result_value()
        return flask.render_template("calculator.html", result=result)

    elif operation == "divide":
        calc.calculator.Calculator.subtract_numbers(values)
        result = calc.calculator.Calculator.get_result_value()
        return flask.render_template("calculator.html", result=result)

    else:
        return flask.render_template("calculator.html")

if __name__ == '__main__': 
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
