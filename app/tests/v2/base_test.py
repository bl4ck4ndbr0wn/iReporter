import json
from unittest import TestCase
from app import create_app
from flask import current_app

from app.api.v2.models.user import User
from instance.db import Model


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
        Model().init_app(_app)
        Model().create_table_user()
        Model().create_table_incident()

        self.user_details = {
            "username": "alpha",
            "password": "password",
            "firstname": "Alpha",
            "lastname": "Nganga",
            "email": "alphanganga@gmail.com"
        }
        self.admin_user = {
            "username": "admin",
            "password": "devpassword",
            "firstname": "Alpha",
            "lastname": "Nganga",
            "email": "alphanganga@gmail.com",
            "is_admin": True
        }
        self.incident = {
            "record_type": "red-flag",
            "location": "1.43434, 9.2343",
            "status": "draft",
            "images": "/photo/1.jpg",
            "videos": "/video/1.mkv",
            "comment": "Police bribe near Ruiru Sports club."
        }
        self.update_incident = {
            "id": 1,
            "record_type": "red-flag",
            "location": "1.0000, 9.0000",
            "status": "draft",
            "images": "/photo/1.jpg",
            "videos": "/video/1.mkv",
            "comment": "Police bribe near Nairobi."
        }
        self.update_incident_status = {
            "id": 1,
            "record_type": "red-flag",
            "location": "1.43434, 9.2343",
            "status": "under investigation",
            "images": "/photo/1.jpg",
            "videos": "/video/1.mkv",
            "comment": "Police bribe near Ruiru Sports club."
        }

    def admin_login(self):
        """
        Makes a request to login endpoint.
        :return: login response data
        """
        u = User(**self.admin_user)
        u.save_to_db()
        self.assertIsNotNone(u.find_by_name('admin'),
                             "Did not find an user with "
                             "name 'admin' after save_to_db")

        response = self.app.post("/api/v2/auth/login",
                                 data=json.dumps({
                                     "username": self.admin_user["username"],
                                     "password": self.admin_user["password"]
                                 }),
                                 headers={'content-type': 'application/json'}
                                 )
        token = json.loads(response.data.decode())
        return token["token"]

    def login(self):
        """
        Makes a request to login endpoint.
        :return: login response data
        """
        response = self.app.post("/api/v2/auth/login",
                                 data=json.dumps({
                                     "username": self.user_details["username"],
                                     "password": self.user_details["password"]
                                                  }),
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def signup(self):
        """
        Makes a request to signup endpoint.
        :return: signup response data
        """
        response = self.app.post("/api/v2/auth/signup",
                                 data=json.dumps(self.user_details),
                                 headers={'content-type': 'application/json'}
                                 )
        return response

    def get_token_on_user_login(self):
        """
        Get token after user logs in
        :return: token(jwt-token)
        """
        self.signup()
        r = self.login()

        token = json.loads(r.data.decode())
        return token["token"]

    def create_incident(self):
        """
        Create new incident function
        :return: response
        """
        token = self.get_token_on_user_login()
        r = self.app.post("/api/v2/interventions",
                          data=json.dumps(self.incident),
                          headers={"content-type": "application/json",
                                   "Authorization": f"Bearer {token}"})
        return r

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
        Model().close_session()
        Model().drop_tables()
        self.app_context.pop()
