from flask import request, jsonify, g
from flask_restful import Resource, reqparse
from app.api.v2.models.incident import Incident
from app.api.v2.models.user import User
from utils.decorators import jwt_required

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('record_type',
                    type=str,
                    required=True,
                    choices=("red-flag", "intervention"),
                    help="This field cannot be left "
                         "blank or Bad choice: {error_msg}"
                    )

parser.add_argument('location',
                    type=str,
                    required=True,
                    help="This field can be left blank!"
                    )

parser.add_argument('status',
                    type=str,
                    required=True,
                    help="This field can be left blank!"
                    )
parser.add_argument('images',
                    action='append',
                    help="This field can be left blank!"
                    )
parser.add_argument('videos',
                    action='append',
                    help="This field can be left blank!"
                    )

parser.add_argument('comment',
                    type=str,
                    required=True,
                    help="This field cannot be left blank!"
                    )


class RedFlagRecords(Resource):
    """
    Fetch a all red-flag record.
    Create a red-flag record.

    :param: incident:
            {
              “id” : Integer,
              “type” : String,       // [red-flag, intervention]
              “location” : String,   // Lat Long coordinates
              “status” : String,     // [draft,
              under investigation, resolved, rejected]
              “Images” : [Image, Image],
              “Videos” : [Image, Image],
              “comment” : String
            }
    :returns records and success massage in json format.
    """

    @jwt_required
    def get(self):
        items = Incident().find_all_by_user_id(g.user.get("user_id"))
        if items:
            return {"status": 200,
                    "data": [incident.serialize() for incident in items]
                    }, 200
        return {"status": 200,
                "data": []
                }, 200

    @jwt_required
    def post(self):
        data = parser.parse_args()
        new_record = Incident(user_id=g.user.get("user_id"), **data)
        new_record.save_to_db()

        return {"status": 201,
                "data": [{
                    "message": "{} record created "
                               "Successfully.".format(new_record.record_type)
                }]}, 201

        # if 'Authorization' in request.headers:
        #     auth_header = request.headers.get('Authorization')
        #     access_token = auth_header.split(" ")[1]
        #     if access_token:
        #         # Attempt to decode the token and get the User ID
        #         user_id = User.decode_token(access_token)
        #         if not isinstance(user_id, str):
        #             # Go ahead and handle the request, the user is authenticated
        #
        #
        #         else:
        #             # user is not legit, so the payload is an error message
        #             response = {
        #                 'message': user_id
        #             }
        #             return jsonify(response), 401
        # return {'message': 'Authorization header is missing in this request.'}, 403
