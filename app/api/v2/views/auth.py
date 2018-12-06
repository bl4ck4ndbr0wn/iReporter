from flask_restful import Resource, reqparse
from app.api.v2.models.user import User

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('username', type=str, required=True,
                    help='This field cannot be left blank!')
parser.add_argument('password', type=str, required=True,
                    help='This field cannot be left blank!')


class SignUp(Resource):
    parser.add_argument('firstname', type=str, required=True,
                        help='This field can be left blank!')

    parser.add_argument('lastname', type=str, required=True,
                        help='This field can be left blank!')

    parser.add_argument('othername', type=str, default="",
                        help='This field can be left blank!')

    parser.add_argument('email', type=str, required=True,
                        help='This field can be left blank!')

    parser.add_argument('phonenumber', type=str, default=0,
                        help='This field can be left blank!')

    def post(self):
        request_data = parser.parse_args()
        u = User().find_by_name(request_data["username"])
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
