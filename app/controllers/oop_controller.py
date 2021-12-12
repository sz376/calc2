"""controls the oop terms page"""
from flask import render_template
from app.controllers.controller import ControllerBase # pylint: disable=no-name-in-module, import-error

class OopGlossController(ControllerBase):
    # pylint: disable=too-few-public-methods
    """class for handling a page"""
    @staticmethod
    def get():
        """returns the oop glossary page"""
        return render_template('oop.html')
