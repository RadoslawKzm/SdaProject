# built-in imports
from dateutil import parser
from typing import Dict, List, Union

# pip3 imports
import requests


def exctractor(*, input_dict):
    """Extract from input given keys and create a list[dicts]
    example dict:
    {"gender":female,
    "first_name":"Marek",
    "letters_in_name":["M","a","r","e","k"]
    "last_name":"Mostowiak",
    "reverted_last_name":"KAIWOTSOm" # reverse letters from last to first and revert uppercase<=>lowercase
    "email":"marek@gmail.com",
    "age":69,
    "birthday":"30-2-1969",
    "nationality":"PL",
    "login":"mareczeq69",
    "password":"one_of_a_kind",
    "city":"Zlotystok",
    "street":"wspolna",
    "number":69,
    "country":"Polandia"
    }

    Be careful about datatypes expected
"""
    input_results: list = input_dict["results"]
    new_list = []
    for dictio in input_results:
        date = parser.parse(dictio["dob"]["date"])
        new_dict = {"gender": dictio["gender"],
                    "first_name": dictio["name"]["first"],
                    "letters_in_name": [letter for letter in dictio["name"]["first"]],
                    "last_name": dictio["name"]["last"],
                    "reverted_last_name": "".join([letter.lower() if letter.isupper() else letter.upper()
                                           for letter in dictio["name"]["last"][::-1]]),
                    "email": dictio["email"],
                    "age": dictio["dob"]["age"],
                    "birthday": f"{date.day}-{date.month}-{date.year}",
                    "nationality": dictio["nat"],
                    "login": dictio["login"]["username"],
                    "password": dictio["login"]["password"],
                    "city": dictio["location"]["city"],
                    "street": dictio["location"]["street"]["name"],
                    "number": dictio["location"]["street"]["number"],
                    "country": dictio["location"]["country"]

                    }
        new_list.append(new_dict)
    return new_list


if __name__ == '__main__':
    # response = requests.get("https://randomuser.me/api/?results=50")
    # test_input = response.json()
    # test_output = exctractor(input_dict=test_input)
    test_input = {"results":[{
        "gender": "female",
        "name": {"title": "Ms", "first": "Madison", "last": "Mcdonalid"},
        "location": {
            "street": {"number": 9258, "name": "Mockingbird Ln"},
            "city": "Port Macquarie",
            "state": "Victoria",
            "country": "Australia",
            "postcode": 3551,
            "coordinates": {"latitude": "-85.0925", "longitude": "8.5685"},
            "timezone": {"offset": "+7:00", "description": "Bangkok, Hanoi, Jakarta"},
        },
        "email": "madison.mcdonalid@example.com",
        "login": {
            "uuid": "a9dce8ad-8253-4e93-a5d4-31aee4683b5b",
            "username": "crazyduck195",
            "password": "stratus",
            "salt": "hwm6KoOx",
            "md5": "4982d237230525ba56a3b096a0ecb25b",
            "sha1": "ae22fbd76c2be7aeeeb0800b4b2b7e61d7f9f130",
            "sha256": "d2d7d32383a524f96e70466ce7df90d7fc8c788f91d87904c2543cf93629a8db",
        },
        "dob": {"date": "1978-12-05T15:47:03.820Z", "age": 43},
        "registered": {"date": "2018-05-31T02:19:03.774Z", "age": 3},
        "phone": "02-3527-3788",
        "cell": "0436-858-501",
        "id": {"name": "TFN", "value": "970368843"},
        "picture": {
            "large": "https://randomuser.me/api/portraits/women/90.jpg",
            "medium": "https://randomuser.me/api/portraits/med/women/90.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/women/90.jpg",
        },
        "nat": "AU",
    }]}
    test_output = exctractor(input_dict=test_input)
    assert test_output[0]["first_name"] == "Madison"
    assert test_output[0]["letters_in_name"] == ["M", "a", "d", "i", "s", "o", "n"]
    assert test_output[0]["last_name"] == "Mcdonalid"
    assert test_output[0]["reverted_last_name"] == "DILANODCm"
    assert test_output[0]["age"] == 43
    assert test_output[0]["login"] == "crazyduck195"
    assert test_output[0]["password"] == "stratus"
    assert test_output[0]["street"] == "Mockingbird Ln"
    assert test_output[0]["number"] == 9258
    assert test_output[0]["country"] == "Australia"
