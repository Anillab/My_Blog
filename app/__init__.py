import flask
from flask  import *
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
# from main  import hello
# from app import errors
bootstrap=Bootstrap()
db=SQLAlchemy()
from .main import main as main_blueprint
def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    app.register_blueprint(main_blueprint)
    return app
