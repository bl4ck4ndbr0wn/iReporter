from flask_restful import Resource


class AllRecords(Resource):
    def get(self):
        return {"status": 200, "message": "Hello, Alpha"}, 200
