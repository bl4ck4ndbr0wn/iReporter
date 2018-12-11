from app.tests.v2.base_test import BaseTest


class TestPage(BaseTest):
    def test_home_page(self):
        """ Home page should respond with a success 200. """
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
