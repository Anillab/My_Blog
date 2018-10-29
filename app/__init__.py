import flask
from flask  import *
from flask_bootstrap import Bootstrap
from config import config_options
# from main  import hello
# from app import errors
bootstrap=Bootstrap()
from .main import main as main_blueprint
def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config_options[config_name])
    app.register_blueprint(main_blueprint)
    return app
