from unittest import TestCase
from app import create_app
from flask import current_app


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
        self.app_context.pop()
