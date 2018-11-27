from instance.tests import assert_status_code_message
import json


class TestUser(object):
    def test_login(self, client):
        """
        Log a specific user in.

        :param client: Flask client
        :param username: The username
        :type username: str
        :param password: The password
        :type password: str
        :return: Flask response
        """
        user = dict(username="alpha@gmail.com", password="alpha123")

        response = client.post("/api/v1/auth/login",
                               data=json.dumps(user),
                               headers={'content-type': 'application/json'}
                               )
        print(response)

        assert response.status_code == 200
