from app.tests.v2.base_test import BaseTest
from app.api.v2.models.incident import Incident
from app.api.v2.models.user import User


class RecordTest(BaseTest):

    def test_crud(self):
        """
        Test CRUD functionality of the class

        :return: Item found.
        """
        u = User(**self.user_details)
        u.save_to_db()
        u.find_by_name('alpha')
        record = Incident(user_id=u.id, **self.incident)

        self.assertIsNone(Incident().find_by_id(1),
                          "Found an Incident with id '1' before save_to_db")

        record.save_to_db()

        self.assertEqual(record.record_type, 'red-flag')
        self.assertIsNotNone(Incident().find_by_id(1),
                             "Did not find an Incident with"
                             " id '1' after save_to_db")

    def test_incident_repr(self):
        """
        testing this function makes an attempt
        to return a string that would yield an
        object with the same value when passed to

        :return: a printable representation of the object
        """
        u = User(**self.user_details)
        u.save_to_db()
        u.find_by_name('alpha')
        u = Incident(user_id=u.id, **self.incident)

        self.assertEqual(str(u),
                         "Police bribe near Ruiru Sports club."
                         " incident in incident Model.")

