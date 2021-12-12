"""controls the command line page"""
from flask import render_template
from app.controllers.controller import ControllerBase # pylint: disable=no-name-in-module, import-error

class CmdLineController(ControllerBase):
    # pylint: disable=too-few-public-methods
    """class for handling a page"""
    @staticmethod
    def get():
        """returns command line page"""
        return render_template('command_line.html')
