from flask import Flask
from flask_restful import Api
from instance.config import config
from app.api.v2.views.auth import SignUp


def create_app(config_name):
    """
    Create a Flask application using the app factory pattern.

    :param: config_name: str
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])

    # initialize

    # Add blueprints
    from app.api import api_bp as api_blueprint
    api = Api(api_blueprint)

    # Register blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api/v2")

    # Url Routes
    routes(api)

    return app


def routes(api):
    """
    Add api routes

    :param api: registered blueprint
    :return: None
    """
    api.add_resource(SignUp, "/auth/register")

    return None
