
from app.tests.v1.base_test import BaseTest

from app.api.v1.models.user import User


class UserTest(BaseTest):

    def test_user_create(self):
        u = User(username="Alpha", password="password")

        self.assertEqual(u.username, "Alpha",
                         "The name of the user after creation does not equal the constructor argument.")
