import json
from app.tests.v1.base_test import BaseTest
from app.api.v1.models.incident import Incident


class RecordTest(BaseTest):
    incident = {
                "record_type": "red-flag",
                "location": "1.43434, 9.2343",
                "status": "draft",
                "images": [
                    {"path": "/photo/1.jpg"},
                    {"path": "/photo/2.jpg"}
                ],
                "videos": [
                    {"path": "/video/1.mkv"},
                    {"path": "/video/2.mkv"}
                ],
                "comment": "Police bribe near Ruiru Sports club.{Kidding.}"
               }

    update_incident = {
        "record_type": "red-flag",
        "location": "1.0000, 9.0000",
        "status": "draft",
        "images": [
            {"path": "/photo/1.jpg"},
            {"path": "/photo/2.jpg"}],
        "videos": [
            {"path": "/video/1.mkv"},
            {"path": "/video/2.mkv"}],
        "comment": "Police bribe near Nairobi.{Kidding.}"
    }

    def login(self):
        """
        Makes a request to login endpoint.

        :return: login response data
        """
        response = self.app.post("/api/v1/auth/login",
                                 data=json.dumps({"username": "alpha",
                                                  "password": "password"
                                                  }),
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def signup(self):
        """
        Makes a request to signup endpoint.

        :return: signup response data
        """
        user = {"firstname": "alpha2",
                "lastname": "nganga",
                "email": "alphanganga@gmail.com",
                "username": "alpha2",
                "password": "password"
                }
        response = self.app.post("/api/v1/auth/register",
                                 data=json.dumps(user),
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def get_user_token(self):
        """
        Get token after user logs in

        :return: token(jwt-token)
        """
        self.signup()
        r = self.login()

        token = json.loads(r.data).get("token", None)
        return token

    def test_incident_found(self):
        """
        Testing if records exist

        :return: status code 200
        """
        token = self.get_user_token()

        self.create_incident()
        r = self.app.get("/api/v1/red-flags",
                         headers={"Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 200)

    def create_incident(self):
        """
        Create new incident function

        :return: response
        """
        token = self.get_user_token()

        r = self.app.post("/api/v1/red-flags",
                          data=json.dumps(RecordTest.incident),
                          headers={"content-type": "application/json",
                                   "Authorization": f"Bearer {token}"})
        return r

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
        self.assertIsNotNone(Incident.find_by_id(3))
        self.assertDictEqual(expected, json.loads(r.data))

    def test_get_specific_incident(self):
        """
        Test to fetch a specific read-flag record
        :param red-flag-id: int
        :return: record.
        """
        token = self.get_user_token()

        self.create_incident()
        r = self.app.get("/api/v1/red-flags/3",
                         headers={"Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 200)
        # self.assertDictEqual({"status": 200,
        #                       "data": [RecordTest.incident]},
        #                      json.loads(r.data))

    def test_specific_record_not_found(self):
        """
        Test if record does not exist

        :return: Error
        """

        token = self.get_user_token()
        r = self.app.get("/api/v1/red-flags/2",
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
        token = self.get_user_token()
        r = self.app.patch("/api/v1/red-flags/3/comment",
                           data=json.dumps(RecordTest.update_incident),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {token}"})

        print(r)
        self.assertEqual(r.status_code, 202)
        self.assertDictEqual({"status": 202,
                              "data": [
                                    {
                                        "id": 3,
                                        "message": "Updated red-flag record’s comment."
                                    }
                                ]
                              },
                             json.loads(r.data))

    def test_incident_update_comment_not_found(self):
        """
        Test incident updated successfully

        :return: Object
        """
        token = self.get_user_token()
        r = self.app.patch("/api/v1/red-flags/10/comment",
                           data=json.dumps(RecordTest.update_incident),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {token}"})

        print(r)
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
        token = self.get_user_token()
        r = self.app.patch("/api/v1/red-flags/3/location",
                           data=json.dumps(RecordTest.update_incident),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 202)
        self.assertDictEqual({"status": 202,
                              "data": [
                                    {
                                        "id": 3,
                                        "message": "Updated red-flag record’s location"
                                    }
                                ]
                              },
                             json.loads(r.data))

    def test_incident_update_location_not_found(self):
        """
        Test incident updated successfully

        :return: Object
        """
        token = self.get_user_token()
        r = self.app.patch("/api/v1/red-flags/10/location",
                           data=json.dumps(RecordTest.update_incident),
                           headers={"content-type": "application/json",
                                    "Authorization": f"Bearer {token}"})

        print(r)
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
        token = self.get_user_token()
        r = self.app.delete("/api/v1/red-flags/1",
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

        token = self.get_user_token()
        r = self.app.delete("/api/v1/red-flags/2",
                            headers={"Authorization": f"Bearer {token}"})

        self.assertEqual(r.status_code, 404)
        self.assertDictEqual({"status": 404,
                              "data": [{
                                   "message": "Incident record Not Found."
                              }]},
                             json.loads(r.data))
