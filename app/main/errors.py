from flask import *
from . import main
@main.errorhandler(404)
def bad_path(error):
    return render_template('fourOwfour.html'),404
