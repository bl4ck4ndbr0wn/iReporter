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
