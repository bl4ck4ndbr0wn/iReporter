import json
from app.tests.v2.base_test import BaseTest
from app.api.v2.models.user import User


class UserTest(BaseTest):
    def test_user_register(self):
        """clear
        Test Signup api.
        :return Success status
        """
        response = self.signup()
        self.assertEqual(response.status_code, 201)
        self.assertDictEqual({"status": 201,
                              "data": [{
                                    "message": "User created Successfully."
                              }]},
                             json.loads(response.data))

    def test_user_register_User_exist(self):
        """
        Test if user exist on create user
        :return: 202
        """
        self.signup()
        response = self.signup()
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual({"status": 400,
                              "data": [{
                                    "message": "A user with "
                                               "that username already exists"
                                }]
                              },
                             json.loads(response.data))

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
                                    "message": "A user with that"
                                               " username already exists"
                                  }
                              ]},
                             json.loads(user_b.data),
                             "The response data is not the same."
                             )


