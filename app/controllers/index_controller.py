"""controls the index page"""
from flask import render_template
from app.controllers.controller import ControllerBase # pylint: disable=no-name-in-module, import-error

class IndexController(ControllerBase):
    # pylint: disable=too-few-public-methods
    """class for handling a page"""
    @staticmethod
    def get():
        """returns the main page"""
        return render_template('index.html')
