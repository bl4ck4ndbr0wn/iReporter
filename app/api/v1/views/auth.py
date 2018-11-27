import datetime
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from app.api.v1.models.user import User


class UserLogin(Resource):
    """
    User login api, that checks if user exists,
    and returns an encrypted user details as a token.
    The create_access_token() function is used to actually
    generate the token.

    :return: access token
    """
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True,
                        help="Username Field is Required.")
    parser.add_argument("password", type=str, required=True,
                        help="Password Field is Required.")

    def post(self):
        data = UserLogin.parser.parse_args()
        u = User.find_by_identity(data['username'])
        if u and User.authenticated(password=data["password"]):
            # Identity can be any data that is json serializable
            access_token = create_access_token(
                user.username, expires_delta=datetime.timedelta(minutes=60))

            return {"status": 200,
                    "token": token,
                    "message": f'You were successfully logged in {username}'}, 200

        return {"status": 400,
                "error": "A user with that username does not exists"
                }, 400
