from app.tests.v1.base_test import BaseTest
from app.api.v1.models.incident import Incident


class RecordTest(BaseTest):
    incident = {
                "record_type": "red-flag",
                "location": "1.43434, 9.2343",
                "status": "draft",
                "images": [
                    {"path": "/photo/1.jpg"},
                    {"path": "/photo/2.jpg"}],
                "videos": [
                    {"path": "/video/1.mkv"},
                    {"path": "/video/2.mkv"}],
                "comment": "Police bribe near Ruiru Sports club.{Kidding.}"
               }

    def test_crude(self):
        """
        Test CRUD functionality of the class
        :return: Item found.
        """
        record = Incident(**RecordTest.incident)

        self.assertIsNone(Incident.find_by_id(1),
                          "Found an Incident with id '1' before save_to_db")

        record.save_to_db()

        self.assertEqual(record.record_type, 'red-flag')
        self.assertIsNotNone(Incident.find_by_id(1),
                             "Did not find an Incident with"
                             " id '1' after save_to_db")

    def test_incident_repr(self):
        """
        testing this function makes an attempt
        to return a string that would yield an
        object with the same value when passed to
        :return: a printable representation of the object
        """
        u = Incident(**RecordTest.incident)

        self.assertEqual(str(u),
                         "Police bribe near Ruiru Sports club."
                         "{Kidding.} incident in incident Model.")
