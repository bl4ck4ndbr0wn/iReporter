from flask import g
from flask_restful import Resource, reqparse
from app.api.v2.models.incident import Incident
from utils.decorators import jwt_required, admin_access
from utils.validation import validate_create_incident, validate_update_incident

parser = reqparse.RequestParser(bundle_errors=True)
update_location_parser = reqparse.RequestParser(bundle_errors=True)
update_comment_parser = reqparse.RequestParser(bundle_errors=True)
update_status_parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('title',
                    type=str,
                    required=True,
                    help="This field cannot be left blank "
                    )
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
            response = []
            for data in items:
                response.append({
                    "id": data[0],
                    "user_id": data[1],
                    "title": data[2],
                    "record_type": data[3],
                    "location": data[4],
                    "status": data[5],
                    "comment": data[6]
                })
            return {"status": 200,
                    "data": response
                    }
        return {"status": 200,
                "data": []
                }, 200

    @jwt_required
    def post(self):
        data = parser.parse_args()

        errors = validate_create_incident(data)
        if errors:
            return {"status": 404,
                    "message": errors
                    }, 404

        new_record = Incident(user_id=g.user.get("user_id"), **data)
        new_record.save_to_db()

        return {"status": 201,
                "data": [new_record.serialize()],
                "message": "{} record created "
                           "Successfully.".format(new_record.record_type)
                }, 201


class RedFlagRecord(Resource):
    """
    Fetch a a specific red-flag record.
    Delete a specific red flag record.

    :param: red_flag_id: red_flag_id
    :returns: record and success massage in json format.
    """

    @jwt_required
    def get(self, intervention_id):
        incident = Incident().find_by_id(intervention_id)
        if incident:
            return {"status": 200,
                    "data": incident.serialize()
                    }
        return {"status": 404,
                "data": [{
                     "message": "Incident record does not exist."
                }]}, 404

    @jwt_required
    def delete(self, intervention_id):
        incident = Incident().find_by_id(intervention_id)
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


class RedFlagRecordLocation(Resource):
    update_location_parser.add_argument('location',
                                        type=str,
                                        required=True,
                                        help="This field can be left blank!"
                                        )

    @jwt_required
    def patch(self, intervention_id):
        data = update_location_parser.parse_args()

        errors = validate_update_incident(data)
        if errors:
            return {"status": 404,
                    "message": errors
                    }, 404

        incident = Incident().find_by_id(intervention_id)
        if incident:
            incident.update_location(data["location"])
            return {
                      "status": 202,
                      "data": [{
                         "id": incident.id,  # red-flag record primary key
                         "message": "Updated red-flag record’s location"
                      }]
                    }, 202

        return {"status": 404,
                "data": [{
                    "message": "Incident record Not Found."
                }]}, 404


class RedFlagRecordComment(Resource):
    update_comment_parser.add_argument('comment',
                                       type=str,
                                       required=True,
                                       help="This field can be left blank!"
                                       )

    @jwt_required
    def patch(self, intervention_id):
        data = update_comment_parser.parse_args()

        errors = validate_update_incident(data)
        if errors:
            return {"status": 404,
                    "message": errors
                    }, 404

        incident = Incident().find_by_id(intervention_id)
        if incident:
            incident.update_comment(data["comment"])
            return {
                      "status": 202,
                      "data": [{
                         "id": incident.id,  # red-flag record primary key
                         "message": "Updated red-flag record’s comment."
                      }]
                    }, 202

        return {"status": 404,
                "data": [{
                    "message": "Incident record Not Found."

                }]}, 404


class RedFlagRecordStatus(Resource):
    update_status_parser.add_argument('status',
                                      type=str,
                                      required=True,
                                      help="This field can be left blank!"
                                      )

    @jwt_required
    @admin_access
    def patch(self, intervention_id):
        data = update_status_parser.parse_args()

        errors = validate_update_incident(data)
        if errors:
            return {"status": 404,
                    "message": errors
                    }, 404

        incident = Incident().find_by_id(intervention_id)
        if incident:
            if incident.record_type[0] != "red-flag":
                return {"status": 401,
                        "error": "This incident record is not a red-flag."
                        }, 401

            incident.update_status(data["status"])
            return {
                      "status": 202,
                      "data": [{
                         "id": incident.id,  # red-flag record primary key
                         "message": "Updated red-flag record status."
                      }]
                    }, 202

        return {"status": 404,
                "data": [{
                    "message": "Incident record Not Found."

                }]}, 404


class InterventionsRecordStatus(Resource):

    @jwt_required
    @admin_access
    def patch(self, intervention_id):
        data = update_status_parser.parse_args()

        errors = validate_update_incident(data)
        if errors:
            return {"status": 404,
                    "message": errors
                    }, 404

        incident = Incident().find_by_id(intervention_id)
        if incident:
            if incident.record_type[0] != "intervention":
                return {"status": 401,
                        "error": "This incident record is not an intervention."
                        }, 401

            incident.update_status(data["status"])
            return {
                       "status": 202,
                       "data": [{
                           "id": incident.id,  # red-flag record primary key
                           "message": "Updated red-flag record status."
                       }]
                   }, 202

        return {"status": 404,
                "data": [{
                    "message": "Incident record Not Found."

                }]}, 404
