from app.tests.v1.base_test import BaseTest

from app.api.v1.models.user import User


class UserTest(BaseTest):

    def test_user_repr(self):
        u = User(username="alpha", password="password")

        self.assertEqual(str(u), "alpha in User Model.")

    def test_user_create(self):
        u = User(username="alpha", password="password")

        self.assertIsNone(User.find_by_name('alpha'),
                          "Found an user with name 'alpha' before save_to_db")
        self.assertIsNone(User.find_by_id(1),
                          "Found an user with id '1' before save_to_db")

        u.save_to_db()

        self.assertIsNotNone(User.find_by_name('alpha'),
                             "Did not find an user with name 'alpha' after save_to_db")
        self.assertIsNotNone(User.find_by_id(1),

                             "Did not find an user with id '1' after save_to_db")
