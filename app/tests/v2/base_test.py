from unittest import TestCase
from app import create_app
from flask import current_app
from instance.db import Model

model = Model()


class BaseTest(TestCase):
    """
    Base Test

    It allows for installation of the database dynamically
    and make sure it is a new blank database each time.
    """

    def setUp(self):
        """
        Setup our flask test app, this only gets executed once.
        Method called to prepare the test fixture.
        Exception raised by this method will be considered an
        error rather than a test failure

        :return: Flask app
        """
        # getting a test client
        _app = create_app("testing")

        # Establish an application context before running the tests.
        # Get a test client
        self.app = _app.test_client()
        self.app_context = _app.app_context()
        self.app_context.push()
        with self.app_context:
            model.drop_tables()
            model.create_table_user()
            model.create_table_incident()

        self.user_details = {
            "firstname": "Alpha",
            "lastname": "Nganga",
            "username": "alpha",
            "password": "password",
            "email": "alphanganga@gmail.com"
        }
        self.incident = {
            "user_id": 1,
            "record_type": "red-flag",
            "location": "1.43434, 9.2343",
            "status": "draft",
            "images": "/photo/1.jpg",
            "videos": "/video/1.mkv",
            "comment": "Police bribe near Ruiru Sports club."
        }
        self.update_incident = {
            "id": 9,
            "record_type": "red-flag",
            "location": "1.0000, 9.0000",
            "status": "draft",
            "images": "/photo/1.jpg",
            "videos": "/video/1.mkv",
            "comment": "Police bribe near Nairobi."
        }

    def test_app_exists(self):
        """
        Testing for the presence of the app context
        """
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        """
        Testing if the config mode is testing
        """
        self.assertTrue(current_app.config['TESTING'])

    def tearDown(self):
        """
        Destroy app context after testing is done
        It's called immediately after the test method
        has been called and the result recorded.
        It's called if the setUp() succeeds,
        regardless of the outcome of the test method.
        """
        model.drop_tables()
        model.close_session()
        self.app.app_context.pop()
