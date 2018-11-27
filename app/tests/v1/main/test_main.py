import json


class TestMain(object):
    def test_all_records(self, client):
        """ All Records route should return a success 200. """
        response = client.get("/api/v1/")
        assert response.status_code == 200
        assert json.loads(response.get_data()) == {
            "status": 200, "message": "Hello, Alpha"}
