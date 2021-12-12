"""controls the oop principles page"""
from flask import render_template
from app.controllers.controller import ControllerBase # pylint: disable=no-name-in-module, import-error

class OopController(ControllerBase):
    # pylint: disable=too-few-public-methods
    """class for handling a page"""
    @staticmethod
    def get():
        """returns oop principles"""
        return render_template('oop_principles.html')
