# built in imports
from unittest.mock import patch, MagicMock

# pip3 install imports
from fastapi.testclient import TestClient

# user created imports
from App.code_folder.main import app
from App.tests.test_main_app import input_data
# from App.tests.test_main_app import output_data


client = TestClient(app)

def test_api():
    response_object_mock = MagicMock()
    response_object_mock.json.return_value = input_data.imgw_request_mock
    response_object_mock.status_code = 200

    request_mock = MagicMock()
    request_mock.get.return_value = response_object_mock
    with patch("App.code_folder.main.requests", request_mock):
        response = client.get("/get")
    assert response.json() == input_data.imgw_request_mock
