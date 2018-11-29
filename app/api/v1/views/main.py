from flask_restful import Resource, reqparse

from app.api.v1.models.incident import Incident


parser = reqparse.RequestParser()
parser.add_argument('record_type',
                    type=str,
                    required=True,
                    help="This field cannot be left blank!"
                    )

parser.add_argument('location',
                    type=str,
                    help="This field cannot be left blank!"
                    )

parser.add_argument('status',
                    type=str,
                    help="This field cannot be left blank!"
                    )

parser.add_argument('comment',
                    type=str,
                    help="This field cannot be left blank!"
                    )


class CreateRecord(Resource):
    def post(self):
        data = parser.parse_args()

        new_record = Incident(**data)
        new_record.save_to_db()

        return {"status": 201,
                "data": [{
                    "id": new_record.id,  # User account primary key
                    "message": "{} record created Successfully.".format(new_record.record_type)
                }]}, 200

    def delete(self):
        return {"status": 200,
                "data": [{
                    "id": 1,  # User account primary key
                    "message": "User created Successfully."
                }]}, 200