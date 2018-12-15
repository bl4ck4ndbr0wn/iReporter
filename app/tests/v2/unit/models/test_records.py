from app.tests.v2.base_test import BaseTest
from app.api.v2.models.incident import Incident


class RecordTest(BaseTest):

    def test_create_record(self):
        """
        Test that the on create a new record, that each value
        passed to similar to the object values

        :return: true is similar
        """
        record = Incident(**self.incident)

        self.assertEqual(record.record_type, "red-flag",
                         "The name of the Incident after creation does"
                         " not equal the constructor argument.")
        self.assertEqual(record.location, "1.43434, 9.2343",
                         "The name of the Incident after creation does"
                         " not equal the constructor argument.")
        self.assertEqual(record.status, "draft",
                         "The name of the Incident after creation does"
                         " not equal the constructor argument.")
        self.assertEqual(record.images, "/photo/1.jpg",
                         "The name of the Incident after creation does"
                         " not equal the constructor argument.")
        self.assertEqual(record.videos, "/video/1.mkv",
                         "The name of the Incident after creation does"
                         " not equal the constructor argument.")
        self.assertEqual(record.comment,
                         "Police bribe near Ruiru Sports club.",
                         "The name of the Incident after creation does"
                         " not equal the constructor argument.")

    def test_incident_json(self):
        """
        Test the json representation of the object created.

        :return: object data in json format
        """
        record = Incident(**self.incident)
        expected = {'comment': 'Police bribe near Ruiru Sports club.',
                     'id': None,
                     'image_path': '/photo/1.jpg',
                     'location': '1.43434, 9.2343',
                     'record_type': 'red-flag',
                     'status': 'draft',
                     'title': 'corruption',
                     'user_id': None,
                     'video_path': '/video/1.mkv'}
        self.assertEqual(record.serialize(), expected,
                         "The JSON export of the Incident is incorrect."
                         " Received {}, expected {}.".format(record.serialize(),
                                                             expected)
                         )

