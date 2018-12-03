from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from instance.config import config

from app.api.v1.views.incident import (RedFlagRecords, RedFlagRecord, RedFlagRecordLocation, RedFlagRecordComment)
from app.api.v1.views.auth import (SignIn, SignUp)

jwt = JWTManager()


def create_app(config_name):
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    # app.config.from_pyfile('config.py')

    # initialize
    jwt.init_app(app)

    # Add blueprints
    from app.api import api_bp as api_blueprint
    api = Api(api_blueprint)

    # Register blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    # Url Routes
    routes(api)

    return app


def routes(api):
    """
    Add api routes

    :param api: registered blueprint
    :return: None
    """
    api.add_resource(SignIn, "/auth/login")
    api.add_resource(SignUp, "/auth/register")

    api.add_resource(RedFlagRecords, "/red-flags")
    api.add_resource(RedFlagRecord, "/red-flags/<int:red_flag_id>")

    api.add_resource(RedFlagRecordLocation, "/red-flags/<int:red_flag_id>/location")
    api.add_resource(RedFlagRecordComment, "/red-flags/<int:red_flag_id>/comment")

    return None
