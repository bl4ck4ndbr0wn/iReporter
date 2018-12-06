import json
from app.tests.v2.base_test import BaseTest


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
        self.assertEqual(response.status_code, 202)
        self.assertDictEqual({"status": 202,
                              "data": [{
                                    "message": "A user with "
                                               "that username already exists"
                                }]
                              },
                             json.loads(response.data))

    def test_user_registration_with_duplicate_username(self):
        """
        Test on register duplicate user.
        :return: error message
        """
        self.signup()
        user_b = self.signup()

        self.assertEqual(user_b.status_code, 202)
        self.assertDictEqual({"status": 202,
                              "data": [
                                  {
                                    "message": "A user with that"
                                               " username already exists"
                                  }
                              ]},
                             json.loads(user_b.data),
                             "The response data is not the same."
                             )

    def test_user_login(self):
        """
        Test login after register
        :return Success status
        """
        response = self.signup()
        self.assertEqual(response.status_code, 201)
        response = self.login()

        self.assertEqual(response.status_code, 200)

    def test_unregistered_user_can_not_login(self):
        """
        Test login user doesnt exist
        :return Failed status
        """
        response = self.app.post("/api/v2/auth/login",
                                 data=json.dumps({"username": "alpha21",
                                                  "password": "password"
                                                  }),
                                 headers={'content-type': 'application/json'}
                                 )

        self.assertEqual(response.status_code, 401)
        self.assertDictEqual({"status": 401,
                              "data": [
                                  {
                                      "message": "A user with that"
                                                 " username doesn't exists"
                                  }
                              ]},
                             json.loads(response.data),
                             "The response data is not the same."
                             )

    def test_user_gets_token_on_login(self):
        """
        Get token after user logs in
        :return: token(jwt-token)
        """
        response = self.signup()
        self.assertEqual(response.status_code, 201)

        token = self.get_token_on_user_login()
        self.assertIsNotNone(token)

