import json
from app.tests.v1.base_test import BaseTest

from app.api.v1.models.user import User


class UserTest(BaseTest):

    def login(self):
        response = self.app.post("/auth/login",
                                 data=json.dumps({"username": "alpha",
                                                      "password": "password"
                                                      }),
                                 headers={'content-type': 'application/json'})
        return response

    def test_user_login(self):
        response = self.login()

        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(User.find_by_name("alpha"))

