from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from instance.config import config
from app.api.v2.views.auth import SignUp, SignIn
from app.api.v2.views.incident import (RedFlagRecords,
                                       RedFlagRecord,
                                       RedFlagRecordComment,
                                       RedFlagRecordLocation
                                       )


def create_app(config_name):
    """
    Create a Flask application using the app factory pattern.

    :param: config_name: str
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
    api.add_resource(SignIn, "/auth/login")

    api.add_resource(RedFlagRecords, "/interventions")
    api.add_resource(RedFlagRecord, "/interventions/<int:intervention_id>")
    api.add_resource(RedFlagRecordLocation,
                     "/interventions/<int:intervention_id>/location")
    api.add_resource(RedFlagRecordComment,
                     "/interventions/<int:intervention_id>/comment")
    return None

