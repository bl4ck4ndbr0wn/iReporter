import json
from app.tests.v2.base_test import BaseTest


class RecordTest(BaseTest):

    def test_create_new_incident(self):
        """
        Test create new incident POST Endpoint.
        :return: status code 201 (Created)
        """
        r = self.create_incident()
        expected = {"status": 201,
                    "data": [{
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
        token = self.get_token_on_user_login()
        r = self.app.get("/api/v2/interventions",
                         headers={"Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 200)

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
