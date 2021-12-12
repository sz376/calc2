"""A simple flask web app"""
from flask import Flask
from werkzeug.debug import DebuggedApplication
from app.controllers.index_controller import IndexController # pylint: disable=no-name-in-module, import-error
from app.controllers.calculator_controller import CalculatorController # pylint: disable=no-name-in-module, import-error
from app.controllers.apache_controller import ApacheController # pylint: disable=no-name-in-module, import-error
from app.controllers.command_line_controller import CmdLineController # pylint: disable=no-name-in-module, import-error
from app.controllers.oop_principles_controller import OopController # pylint: disable=no-name-in-module, import-error
from app.controllers.oop_controller import OopGlossController # pylint: disable=no-name-in-module, import-error

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():
    """main page"""
    return IndexController.get()

@app.route("/apache")
def apache_get():
    """apache tutorial"""
    return ApacheController.get()

@app.route("/oop")
def azure_get():
    """oop terms"""
    return OopGlossController.get()

@app.route("/command_line")
def cmdline_get():
    """command line guide"""
    return CmdLineController.get()

@app.route("/oop_principles")
def oop_get():
    """principles of oop"""
    return OopController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    """calculator page"""
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    """calculator results"""
    return CalculatorController.post()
