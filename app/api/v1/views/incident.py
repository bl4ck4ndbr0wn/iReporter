from flask_restful import Resource, reqparse
from app.api.v1.models.incident import Incident
from flask_jwt_extended import  jwt_required


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('record_type',
                    type=str,
                    required=True,
                    choices=("red-flag", "intervention"),
                    help="This field cannot be left blank or Bad choice: {error_msg}"
                    )

parser.add_argument('location',
                    type=str,
                    help="This field can be left blank!"
                    )

parser.add_argument('status',
                    type=str,
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
              “status” : String,     // [draft, under investigation, resolved, rejected]
              “Images” : [Image, Image],
              “Videos” : [Image, Image],
              “comment” : String
            }
    :returns records and success massage in json format.
    """

    @jwt_required
    def get(self):
        return {"status": 200,
                "data": [item.json() for item in Incident.get_all()
                         ]
                }, 200

    @jwt_required
    def post(self):
        data = parser.parse_args()

        new_record = Incident(**data)
        new_record.save_to_db()

        return {"status": 201,
                "data": [{
                    "id": new_record.id,  # User account primary key
                    "message": "{} record created Successfully.".format(new_record.record_type)
                }]}, 200


class RedFlagRecord(Resource):
    """
    Fetch a a specific red-flag record.
    Delete a specific red flag record.

    :param: red_flag_id: red_flag_id
    :returns: record and success massage in json format.
    """

    @jwt_required
    def get(self, red_flag_id):
        incident = Incident.find_by_id(red_flag_id)
        if incident:
            return {"status": 200,
                    "data": [incident.json()]
                    }
        return {"status": 404,
                "data": [{
                     "message": "Incident record does not exist."
                }]}, 404

    @jwt_required
    def delete(self, red_flag_id):
        incident = Incident.find_by_id(red_flag_id)
        if incident:
            incident.delete_from_db()
            return {"status": 200,
                    "data": [{
                        "id": incident.id,
                        "message": "Incident record has been deleted."
                    }]}
        return {"status": 404,
                "data": [{
                     "message": "Incident record Not Found."
                }]}, 404
