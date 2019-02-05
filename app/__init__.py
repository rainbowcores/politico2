import os

from flask import Flask
from .v1 import politicalparties


# local import
from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    
    app.register_blueprint(politicalparties.api)
    
    
    return app