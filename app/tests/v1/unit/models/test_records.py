from app.tests.v1.base_test import BaseTest
from app.api.v1.models.incident import Incident


class RecordTest(BaseTest):
    incident = {
                "record_type": "red-flag",
                "location": "1.43434, 9.2343",
                "status": "draft",
                "images": [
                    {"path:": "/photo/1.jpg"},
                    {"path": "/photo/2.jpg"}],
                "videos": [
                    {"path:": "/video/1.mkv"},
                    {"path:": "/video/2.mkv"}],
                "comment": "Police bribe near Ruiru Sports club.{Kidding.}"
               }

    def test_create_record(self):
        """
        Test that the on create a new record, that each value
        passed to similar to the object values

        :return: true is similar
        """
        record = Incident(**RecordTest.incident)

        self.assertEqual(record.record_type, "red-flag",
                         "The name of the Incident after creation does not equal the constructor argument.")
        self.assertEqual(record.location, "1.43434, 9.2343",
                         "The name of the Incident after creation does not equal the constructor argument.")
        self.assertEqual(record.status, "draft",
                         "The name of the Incident after creation does not equal the constructor argument.")
        self.assertEqual(record.images, [{"path:": "/photo/1.jpg"},
                                         {"path": "/photo/2.jpg"}],
                         "The name of the Incident after creation does not equal the constructor argument.")
        self.assertEqual(record.videos, [{"path:": "/video/1.mkv"},
                                         {"path:": "/video/2.mkv"}],
                         "The name of the Incident after creation does not equal the constructor argument.")
        self.assertEqual(record.comment, "Police bribe near Ruiru Sports club.{Kidding.}",
                         "The name of the Incident after creation does not equal the constructor argument.")

    def test_incident_json(self):
        """
        Test the json representation of the object created.

        :return: object data in json format
        """
        record = Incident(**RecordTest.incident)
        RecordTest.incident["id"] = record.id

        expected = RecordTest.incident

        self.assertEqual(record.json(), expected,
                         "The JSON export of the Incident is incorrect. Received {}, expected {}.".format(record.json(),
                                                                                                          expected)
                         )
