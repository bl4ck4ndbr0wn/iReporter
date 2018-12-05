import json
from app.tests.v2.base_test import BaseTest


class RecordTest(BaseTest):
    def __init__(self):
        super().__init__()
        self.token = self.get_token_on_user_login()

    def test_create_new_incident(self):
        """
        Test create new incident POST Endpoint.
        :return: status code 201 (Created)
        """
        r = self.create_incident()
        expected = {"status": 201,
                    "data": [{
                        "id": 3,
                        "message": "red-flag record created Successfully."
                    }]}

        self.assertEqual(r.status_code, 201)
        self.assertDictEqual(expected, json.loads(r.data))

    def test_get_all_incident(self):
        """
        Testing if records exist
        :return: status code 200
        """
        self.create_incident()
        r = self.app.get("/api/v1/red-flags",
                         headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(r.status_code, 200)

    def test_get_specific_incident(self):
        """
        Test to fetch a specific read-flag record
        :param red-flag-id: int
        :return: record.
        """
        self.create_incident()
        r = self.app.get("/api/v1/red-flags/3",
                         headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(r.status_code, 200)

    def test_incident_update_comment(self):
        """
        Test incident updated successfully
        :return: Object
        """
        r = self.app.patch("/api/v1/red-flags/3/comment",
                           data=json.dumps(self.update_incident),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {self.token}"})

        self.assertEqual(r.status_code, 202)
        self.assertDictEqual({"status": 202,
                              "data": [
                                    {
                                        "id": 3,
                                        "message": "Updated red-flag "
                                                   "record’s comment."
                                    }
                                ]
                              },
                             json.loads(r.data))

    def test_incident_update_comment_not_found(self):
        """
        Test incident updated successfully
        :return: Object
        """
        r = self.app.patch("/api/v1/red-flags/10/comment",
                           data=json.dumps(self.update_incident),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {self.token}"})

        self.assertEqual(r.status_code, 404)
        self.assertDictEqual({"status": 404,
                              "data": [
                                    {
                                        "message": "Incident record Not Found."
                                    }
                                ]
                              },
                             json.loads(r.data))

    def test_incident_update_location(self):
        """
        Test incident updated successfully
        :return: Object
        """
        r = self.app.patch("/api/v1/red-flags/3/location",
                           data=json.dumps(self.update_incident),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {self.token}"})

        self.assertEqual(r.status_code, 202)
        self.assertDictEqual({"status": 202,
                              "data": [
                                    {
                                        "id": 3,
                                        "message": "Updated red-flag "
                                                   "record’s location"
                                    }
                                ]
                              },
                             json.loads(r.data))

    def test_incident_update_location_not_found(self):
        """
        Test incident updated successfully
        :return: Object
        """
        r = self.app.patch("/api/v1/red-flags/10/location",
                           data=json.dumps(self.update_incident),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {self.token}"})

        self.assertEqual(r.status_code, 404)
        self.assertDictEqual({"status": 404,
                              "data": [
                                    {
                                        "message": "Incident record Not Found."
                                    }
                                ]
                              },
                             json.loads(r.data))

    def test_delete_specific_record(self):
        """
        Test if successfully deleted
        :return: status_code 200
        """
        self.create_incident()
        r = self.app.delete("/api/v1/red-flags/1",
                            headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(r.status_code, 200)
        self.assertDictEqual({"status": 200,
                             "data": [{
                                 "id": 1,
                                 "message": "Incident record has been deleted."
                             }]},
                             json.loads(r.data))

    def test_deleting_specific_record_not_found(self):
        """
        Test if record does not exist for delete show error
        :return: Error
        """
        r = self.app.delete("/api/v1/red-flags/2",
                            headers={"Authorization": f"Bearer {self.token}"})

        self.assertEqual(r.status_code, 404)
        self.assertDictEqual({"status": 404,
                              "data": [{
                                   "message": "Incident record Not Found."
                              }]},
                             json.loads(r.data))

    def test_admin_can_change_incident_status(self):
        """
        Test incident updated successfully
        :return: Object
        """
        r = self.app.patch("/api/v1/admin/red-flags/3",
                           data=json.dumps(self.update_incident_status),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {self.token}"})

        self.assertEqual(r.status_code, 202)
        self.assertDictEqual({"status": 202,
                              "data": [
                                    {
                                        "id": 3,
                                        "message": "Updated red-flag "
                                                   "record’s comment."
                                    }
                                ]
                              },
                             json.loads(r.data))

    def test_admin_can_change_status_incident_not_found(self):
        """
        Test incident updated successfully
        :return: Object
        """
        r = self.app.patch("/api/v1/admin/red-flags/3",
                           data=json.dumps(self.update_incident_status),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {self.token}"})

        self.assertEqual(r.status_code, 404)
        self.assertDictEqual({"status": 404,
                              "data": [
                                    {
                                        "message": "Incident record Not Found."
                                    }
                                ]
                              },
                             json.loads(r.data))
