from flask import g
from flask_restful import Resource, reqparse
from app.api.v2.models.user import User
from utils.decorators import jwt_required
from utils.validation import validate_login, validate_signup, validate_profile

parser = reqparse.RequestParser(bundle_errors=True)
Login_parser = reqparse.RequestParser(bundle_errors=True)
profile_parser = reqparse.RequestParser(bundle_errors=True)


class SignIn(Resource):
    """
    Authorize a user to access the data.
    :param user:{ “username” : String,
                  “password” : String,
                }
    :returns user
    """
    Login_parser.add_argument('username', type=str, required=True,
                              help='This field cannot be left blank!')
    Login_parser.add_argument('password', type=str, required=True,
                              help='This field cannot be left blank!')

    def post(self):
        """
        Receives data in json format and authenticates the user is exists
        :return: Jwt token and success status
        """
        request_data = Login_parser.parse_args()

        errors = validate_login(request_data)
        if errors:
            return {"status": 404,
                    "message": errors
                    }, 404

        u = User().find_by_name(request_data["username"])

        if u and u.authenticated(password=request_data["password"]):
            token = u.generate_token()
            return {"status": 200,
                    'token': token.decode(),
                    "data": [{
                        'message': f'You were successfully'
                        f' logged in {u.username}'
                    }]}, 200

        return {"status": 401,
                "data": [{
                    "message": "Username or password is incorrect."
                }]}, 401


class SignUp(Resource):
    parser.add_argument('username', type=str, required=True,
                        help='This field cannot be left blank!')
    parser.add_argument('password', type=str, required=True,
                        help='This field cannot be left blank!')
    parser.add_argument('firstname', type=str, required=True,
                        help='This field can be left blank!')

    parser.add_argument('lastname', type=str,required=True,
                        help='This field can be left blank!')

    parser.add_argument('othernames', type=str, default="",
                        help='This field can be left blank!')

    parser.add_argument('email', type=str, required=True,
                        help='This field can be left blank!')

    parser.add_argument('phonenumber', type=str, default=0,
                        help='This field can be left blank!')

    def post(self):
        request_data = parser.parse_args()

        errors = validate_signup(request_data)
        if errors:
            return {"status": 404,
                    "message": errors
                    }, 404

        u = User().find_by_name(request_data["username"])
        if u:
            return {"status": 202,
                    "data": [{
                        "message": "A user with that username already exists"
                    }]}, 202

        user = User(**request_data)
        user.save_to_db()

        return {"status": 201,
                "data": [{
                    "message": "User created Successfully."
                }]}, 201


class Profile(Resource):
    profile_parser.add_argument('firstname', type=str, required=True,
                                help='This field can be left blank!')

    profile_parser.add_argument('lastname', type=str, required=True,
                                help='This field can be left blank!')

    profile_parser.add_argument('othernames', type=str, default="",
                                help='This field can be left blank!')

    profile_parser.add_argument('email', type=str, required=True,
                                help='This field can be left blank!')

    profile_parser.add_argument('phonenumber', type=str, default=0,
                                help='This field can be left blank!')

    @jwt_required
    def patch(self):
        data = profile_parser.parse_args()

        errors = validate_profile(data)
        if errors:
            return {"status": 404,
                    "message": errors
                    }, 404

        user = User().find_by_id(g.user.get("user_id"))
        if user:
            user.update_user(data)
            return {"status": 202,
                    "data": [{
                        "id": user.id,  # red-flag record primary key
                        "message": "Updated User profile Successfully."
                    }]}, 202

        return {"status": 401,
                "message": "A user with that id Doesn't exists"
                }, 401
