from flask_restful import Resource
from flask import jsonify


class AllRecords(Resource):
    def get(self):
        return jsonify({"status": 200, "message": "Hello, Alpha"}), 200
