import json
from app.tests.v1.base_test import BaseTest
from app.api.v1.models.incident import Incident


class RecordTest(BaseTest):
    incident = {
                "record_type": "red-flag",
                "location": "1.43434, 9.2343",
                "status": "draft",
                "images": ["/photo/1.jpg", "/photo/2.jpg"],
                "videos": ["/video/1.mkv", "/video/2.mkv"],
                "comment": "Police bribe near Ruiru Sports club.{Kidding.}"
                }

    def test_incident_not_found(self):
        """
        Testing if a record does not exist

        :return: status code 400
        """
        r = self.app.get("/api/v1/red-flag")

        self.assertEqual(r.status_code, 200)
        self.assertDictEqual({"status": 200,
                              "data": []},
                             json.loads(r.data))

    def test_incident_found(self):
        """
        Testing if records exist

        :return: status code 200
        """
        Incident(**RecordTest.incident).save_to_db()
        r = self.app.get("/api/v1/red-flag")

        self.assertEqual(r.status_code, 200)
        self.assertDictEqual({"status": 200,
                              "data": [RecordTest.incident]},
                             json.loads(r.data))
