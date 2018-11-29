import json
from app.tests.v1.base_test import BaseTest

from app.api.v1.models.user import User


class UserTest(BaseTest):

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

    def test_user_login(self):
        """
        Test login.

        :return Success status
        """
        response = self.login()

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(User.find_by_name("alpha"))

    def test_user_register(self):
        """
        Test Signup api.

        :return Success status
        """
        response = self.signup()

        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(User.find_by_name("alpha"))

    def test_register_duplicate_user(self):
        """
        Test on register duplicate user.

        :return: error message
        """
        self.signup()
        user_b = self.signup()

        self.assertEqual(user_b.status_code, 400)
        self.assertDictEqual({"status": 400,
                              "data": [
                                  {
                                    "message": "A user with that username already exists"
                                  }
                              ]},
                             json.loads(user_b.data),
                             "The response data is not the same."
                             )

