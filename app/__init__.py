

from flask import Flask
from .v1.views.politicalmain import api
from .v1.views import politicaloffices, politicalparties
from app.v2.models.database.database_config import initdb
from app.v2.views.userviews import thisapi as users


from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.app_context().push()
    #app.config.from_pyfile('config.py')
    initdb()

    app.register_blueprint(api)
    app.register_blueprint(users)

    return app
