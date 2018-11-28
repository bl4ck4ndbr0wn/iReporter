from unittest import TestCase

from app.api.v1.models.user import User


class UserTest(TestCase):

    def test_user_repr(self):
        u = User(username="Alpha", password="password")

        self.assertEqual(str(u), "Alpha in User Model.")
