from json_expected_output import expected_output
from json_input import json

from App.code_folder.filter_json import filter_json


def test_positive_case():
    output = filter_json(json, "12600")
    assert output == expected_output
