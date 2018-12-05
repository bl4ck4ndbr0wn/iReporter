from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from instance.config import config


def create_app(config_name):
    """
    Create a Flask application using the app factory pattern.

    :rtype: object
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])

    # initialize
    CORS(app)

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

    return None
