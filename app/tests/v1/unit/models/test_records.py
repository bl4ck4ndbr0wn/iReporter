# from app.tests.v1.base_test import BaseTest
# from app.api.v1.models.incident import Incident
#
#
# class RecordTest(BaseTest):
#     incident = {
#                 "record_type": "red-flag",
#                 "location": "1.43434, 9.2343",
#                 "status": "draft",
#                 "images": [
#                     {"path": "/photo/1.jpg"},
#                     {"path": "/photo/2.jpg"}
#                 ],
#                 "videos": [
#                     {"path": "/video/1.mkv"},
#                     {"path": "/video/2.mkv"}
#                 ],
#                 "comment": "Police bribe near Ruiru Sports club.{Kidding.}"
#                }
#
#     update_incident = {
#         "id": 9,
#         "record_type": "red-flag",
#         "location": "1.0000, 9.0000",
#         "status": "draft",
#         "images": [
#             {"path": "/photo/1.jpg"},
#             {"path": "/photo/2.jpg"}
#         ],
#         "videos": [
#             {"path": "/video/1.mkv"},
#             {"path": "/video/2.mkv"}
#         ],
#         "comment": "Police bribe near Nairobi.{Kidding.}"
#     }
#
#     def test_create_record(self):
#         """
#         Test that the on create a new record, that each value
#         passed to similar to the object values
#
#         :return: true is similar
#         """
#         record = Incident(**incident)
#
#         self.assertEqual(record.record_type, "red-flag",
#                          "The name of the Incident after creation does"
#                          " not equal the constructor argument.")
#         self.assertEqual(record.location, "1.43434, 9.2343",
#                          "The name of the Incident after creation does"
#                          " not equal the constructor argument.")
#         self.assertEqual(record.status, "draft",
#                          "The name of the Incident after creation does"
#                          " not equal the constructor argument.")
#         self.assertEqual(record.images, [{"path": "/photo/1.jpg"},
#                                          {"path": "/photo/2.jpg"}],
#                          "The name of the Incident after creation does"
#                          " not equal the constructor argument.")
#         self.assertEqual(record.videos, [{"path": "/video/1.mkv"},
#                                          {"path": "/video/2.mkv"}],
#                          "The name of the Incident after creation does"
#                          " not equal the constructor argument.")
#         self.assertEqual(record.comment,
#                          "Police bribe near Ruiru Sports club.{Kidding.}",
#                          "The name of the Incident after creation does"
#                          " not equal the constructor argument.")
#
#     def test_incident_json(self):
#         """
#         Test the json representation of the object created.
#
#         :return: object data in json format
#         """
#         record = Incident(**incident)
#         expected = {
#                     "id": record.id,
#                     "record_type": "red-flag",
#                     "location": "1.43434, 9.2343",
#                     "status": "draft",
#                     "images": [
#                         {"path": "/photo/1.jpg"},
#                         {"path": "/photo/2.jpg"}],
#                     "videos": [
#                         {"path": "/video/1.mkv"},
#                         {"path": "/video/2.mkv"}],
#                     "comment": "Police bribe near Ruiru Sports club.{Kidding.}"
#                    }
#
#         self.assertEqual(record.json(), expected,
#                          "The JSON export of the Incident is incorrect."
#                          " Received {}, expected {}.".format(record.json(),
#                                                              expected)
#                          )
#
#     def test_incident_update_comment_and_location(self):
#         """
#         Test incident updated successfully
#
#         :return: Object
#         """
#         record = Incident(**incident)
#         record.save_to_db()
#
#         record.update_comment(update_incident["comment"])
#         record.save_to_db()
#
#         self.assertEqual(record.comment,
#                          update_incident["comment"],
#                          "Update comment failed.")
#
#         record.update_location(update_incident["location"])
#         record.save_to_db()
#
#         self.assertEqual(record.location,
#                          update_incident["location"],
#                          "Update location failed.")
