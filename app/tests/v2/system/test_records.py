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
                        "id": 1,
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
