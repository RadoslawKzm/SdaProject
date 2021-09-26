# built in imports
from unittest.mock import patch, MagicMock

# pip3 install imports
from fastapi.testclient import TestClient

# user created imports
from App.code_folder.main import app
# from App.tests.test_main_app import input_data
# from App.tests.test_main_app import output_data


client = TestClient(app)



def test_api():
    response = client.get("/get")
    request_mock = MagicMock()
    request_mock.get.return_value = 1
    print("pass")

