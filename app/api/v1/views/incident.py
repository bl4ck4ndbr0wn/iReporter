from flask_restful import Resource
from app.api.v1.models.incident import Incident


class RedFlagRecords(Resource):
    """
    Fetch a all red-flag record.
    Create a red-flag record.
    Edit the location, comment of a specific red-flag record.
    Delete a specific red flag record.

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

    def get(self):
        return {"status": 200, "data": Incident.get_all()}, 200

    def post(self):
        pass
