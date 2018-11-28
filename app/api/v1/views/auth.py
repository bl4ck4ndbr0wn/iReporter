import datetime
from flask_restful import Resource, reqparse
from app.api.v1.models.user import User
from flask_jwt_extended import create_access_token

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True,
                    help='This field cannot be left blank!')
parser.add_argument('password', type=str, required=True,
                    help='This field cannot be left blank!')


class SignIn(Resource):
    """
    Authorize a user to access the data.

    :param user:{ “username” : String,
                  “password” : String,
                }
    :returns user
    """

    def post(self):
        """
        Receives data in json format and authenticates the user is exists

        :return: Jwt token and success status
        """
        request_data = parser.parse_args()
        u = User.find_by_name(request_data["username"])

        if u and u.authenticated(password=request_data["password"]):
            expire_time = datetime.timedelta(minutes=60)
            token = create_access_token(u, expires_delta=expire_time)
            return {"status": 200,
                    'token': token,
                    "data": [{
                        'message': f'You were successfully logged in {u.username}'
                    }]}, 200

        return {"status": 400,
                "data": [{
                    "message": "A user with that username already exists"
                }]}, 400
