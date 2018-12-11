import json
from app.tests.v2.base_test import BaseTest


class RecordTest(BaseTest):

    def test_create_new_incident(self):
        """
        Test create new incident POST Endpoint.
        :return: status code 201 (Created)
        """
        r = self.create_incident()

        self.assertEqual(r.status_code, 201)

    def test_get_all_incident(self):
        """
        Testing if records exist
        :return: status code 200
        """
        self.create_incident()
        token = self.get_token_on_user_login()
        r = self.app.get("/api/v2/interventions",
                         headers={"Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 200)

    def test_get_all_incident_empty_list(self):
        """
        Testing if records exist
        :return: status code 200
        """
        token = self.get_token_on_user_login()
        r = self.app.get("/api/v2/interventions",
                         headers={"Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 200)
        self.assertDictEqual({"status": 200,
                              "data": []
                              },
                             json.loads(r.data))

    def test_get_specific_incident(self):
        """
        Test to fetch a specific read-flag record
        :param red-flag-id: int
        :return: record.
        """
        self.create_incident()
        token = self.get_token_on_user_login()
        r = self.app.get("/api/v2/interventions/1",
                         headers={"Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 200)

    def test_specific_record_not_found(self):
        """
        Test if record does not exist
        :return: Error
        """
        token = self.get_token_on_user_login()
        r = self.app.get("/api/v2/interventions/2",
                         headers={"Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 404)
        self.assertDictEqual({"status": 404,
                             "data": [{
                                 "message": "Incident record does not exist."
                             }]},
                             json.loads(r.data))

    def test_incident_update_comment(self):
        """
        Test incident updated successfully
        :return: Object
        """
        r = self.create_incident()
        self.assertEqual(r.status_code, 201)
        token = self.get_token_on_user_login()
        r = self.app.patch("/api/v2/interventions/1/comment",
                           data=json.dumps(self.update_incident),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 202)
        self.assertDictEqual({"status": 202,
                              "data": [
                                    {
                                        "id": 1,
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
        r = self.create_incident()
        self.assertEqual(r.status_code, 201)
        token = self.get_token_on_user_login()
        r = self.app.patch("/api/v2/interventions/2/comment",
                           data=json.dumps(self.update_incident),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {token}"})

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
        r = self.create_incident()
        self.assertEqual(r.status_code, 201)
        token = self.get_token_on_user_login()
        r = self.app.patch("/api/v2/interventions/1/location",
                           data=json.dumps(self.update_incident),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 202)
        self.assertDictEqual({"status": 202,
                              "data": [
                                    {
                                        "id": 1,
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
        r = self.create_incident()
        self.assertEqual(r.status_code, 201)
        token = self.get_token_on_user_login()
        r = self.app.patch("/api/v2/interventions/2/location",
                           data=json.dumps(self.update_incident),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {token}"})

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
        r = self.create_incident()
        self.assertEqual(r.status_code, 201)
        token = self.get_token_on_user_login()
        r = self.app.delete("/api/v2/interventions/1",
                            headers={"Authorization": f"Bearer {token}"})

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
        token = self.get_token_on_user_login()
        r = self.app.delete("/api/v2/interventions/2",
                            headers={"Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 404)
        self.assertDictEqual({"status": 404,
                              "data": [{
                                   "message": "Incident record Not Found."
                              }]},
                             json.loads(r.data))

    def test_admin_can_change_red_flag_status(self):
        """
        Test incident updated successfully
        :return: Object
        """
        r = self.create_incident()
        self.assertEqual(r.status_code, 201)
        token = self.admin_login()
        r = self.app.patch("/api/v2/red-flags/1/status",
                           data=json.dumps(self.update_red_flag_status),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 202)
        self.assertDictEqual({"status": 202,
                              "data": [
                                    {
                                        "id": 1,
                                        "message": "Updated red-flag "
                                                   "record status."
                                    }
                                ]
                              },
                             json.loads(r.data))

    def test_admin_can_change_status_red_flag_not_found(self):
        """
        Test incident updated successfully
        :return: Object
        """
        token = self.admin_login()
        r = self.app.patch("/api/v2/red-flags/2/status",
                           data=json.dumps(self.update_red_flag_status),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 404)
        self.assertDictEqual({"status": 404,
                              "data": [
                                    {
                                        "message": "Incident record Not Found."
                                    }
                                ]
                              },
                             json.loads(r.data))

    def test_admin_can_change_red_flag_status_type_error(self):
        """
        Test incident updated successfully
        :return: Object
        """
        r = self.create_incident()
        self.assertEqual(r.status_code, 201)
        token = self.admin_login()
        r = self.app.patch("/api/v2/red-flags/1/status",
                           data=json.dumps(self.update_intervention_status),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 401)
        self.assertDictEqual({"status": 401,
                              "error": "This incident record is not a red-flag."
                              },
                             json.loads(r.data))

    def test_admin_can_change_interventions_status(self):
        """
        Test incident updated successfully
        :return: Object
        """
        r = self.create_incident()
        self.assertEqual(r.status_code, 201)
        token = self.admin_login()
        r = self.app.patch("/api/v2/interventions/1/status",
                           data=json.dumps(self.update_intervention_status),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 202)
        self.assertDictEqual({"status": 202,
                              "data": [
                                    {
                                        "id": 1,
                                        "message": "Updated red-flag "
                                                   "record status."
                                    }
                                ]
                              },
                             json.loads(r.data))

    def test_admin_can_change_interventions_status_type_error(self):
        """
        Test incident updated successfully
        :return: Object
        """
        r = self.create_incident()
        self.assertEqual(r.status_code, 201)
        token = self.admin_login()
        r = self.app.patch("/api/v2/interventions/1/status",
                           data=json.dumps(self.update_red_flag_status),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 401)
        self.assertDictEqual({"status": 401,
                              "error": "This incident record is not an intervention."
                              },
                             json.loads(r.data))

    def test_admin_can_change_status_interventions_not_found(self):
        """
        Test incident updated successfully
        :return: Object
        """
        token = self.admin_login()
        r = self.app.patch("/api/v2/interventions/2/status",
                           data=json.dumps(self.update_intervention_status),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 404)
        self.assertDictEqual({"status": 404,
                              "data": [
                                    {
                                        "message": "Incident record Not Found."
                                    }
                                ]
                              },
                             json.loads(r.data))
