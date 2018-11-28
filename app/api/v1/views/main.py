from flask_restful import Resource


class RedFlagRecords(Resource):
    """
    Fetch a all red-flag record.
    Create a red-flag record.
    Edit the location, comment of a specific red-flag record.
    Delete a specific red flag record.

    :param: incident:
            {
              “id” : Integer,
              “createdOn” : Date,
              “createdBy” : Integer, // represents the user who created this record
              “type” : String,       // [red-flag, intervention]
              “location” : String,   // Lat Long coordinates
              “status” : String,     // [draft, under investigation, resolved, rejected]
              “Images” : [Image, Image],
              “Videos” : [Image, Image],
              “comment” : String
               ...
            }
    :returns records and success massage in json format.
    """

    def get(self):
        pass

    def post(self):
        pass
