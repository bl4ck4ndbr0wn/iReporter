from app.tests.v1.base_test import BaseTest
from app.api.v1.models.user import User


class UserTest(BaseTest):

    def test_user_create(self):
        """
        Test that the on create a new record, that each value
        passed to similar to the object values

        :return: true is similar
        """
        u = User(username="Alpha", password="password")

        self.assertEqual(u.username,
                         "Alpha",
                         "The name of the user after creation does "
                         "not equal the constructor argument.")
