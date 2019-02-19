import os

from flask import Flask
from .v1.views.politicalmain import api
from .v1.views import politicaloffices, politicalparties
from app.v2.models.database.database_config import initdb


# local import
from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db_url = app_config[config_name].Database_Url
    print("\n\n\n", db_url, "\n\n\n")

    initdb(db_url)
    
    app.register_blueprint(api)

    return app
