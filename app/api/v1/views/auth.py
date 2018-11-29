import datetime
from flask_restful import Resource, reqparse
from app.api.v1.models.user import User
from flask_jwt_extended import create_access_token

parser = reqparse.RequestParser(bundle_errors=True)
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
            token = create_access_token(u.username,
                                        expires_delta=expire_time)
            return {"status": 200,
                    'token': token,
                    "data": [{
                        'message': f'You were successfully'
                        f' logged in {u.username}'
                    }]}, 200

        return {"status": 400,
                "data": [{
                    "message": "A user with that username doesn't exists"
                }]}, 400


class SignUp(Resource):
    parser.add_argument('firstname', type=str, default="",
                        help='This field can be left blank!')

    parser.add_argument('lastname', type=str, default="",
                        help='This field can be left blank!')

    parser.add_argument('othername', type=str, default="",
                        help='This field can be left blank!')

    parser.add_argument('email', type=str, default="",
                        help='This field can be left blank!')

    parser.add_argument('phonenumber', type=str, default="",
                        help='This field can be left blank!')

    def post(self):
        request_data = parser.parse_args()
        u = User.find_by_name(request_data["username"])

        if u:
            return {"status": 400,
                    "data": [{
                        "message": "A user with that username already exists"
                    }]}, 400

        user = User(**request_data)
        user.save_to_db()

        return {"status": 201,
                "data": [{
                    "message": "User created Successfully."
                }]}, 201
