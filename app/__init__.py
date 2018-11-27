from flask import Flask
from flask_restful import Api
from instance.config import config
from flask_jwt_extended import JWTManager

from app.api.v1.views.main import AllRecords
from app.api.v1.views.auth import UserLogin


jwt = JWTManager()


def create_app(config_name):
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])

    # Initialize apps
    config[config_name].init_app(app)
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
    api.add_resource(AllRecords, "/")
    api.add_resource(UserLogin, "/auth/login")
