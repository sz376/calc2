"""controls the calc page"""
from flask import render_template
from app.controllers.controller import ControllerBase # pylint: disable=no-name-in-module, import-error

class ApacheController(ControllerBase):
    # pylint: disable=too-few-public-methods
    """class for handling a page"""
    @staticmethod
    def get():
        """returns the apache page"""
        return render_template('apache.html')
