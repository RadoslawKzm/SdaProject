# built-in imports
from typing import Dict

# pip3 imports
import requests
from pydantic import BaseModel


"""Create python model representation of randomuser output using pydantic model"""


class Picture(BaseModel):
    """Fill it with results[x]['picture'] things and types"""


class Id(BaseModel):
    """Fill it with results[x]['id'] things and types"""


class Registered(BaseModel):
    """Fill it with results[x]['registered'] things and types"""


class Dob(BaseModel):
    """Fill it with results[x]['dob'] things and types"""


class Login(BaseModel):
    """Fill it with results[x]['login'] things and types"""


class Timezone(BaseModel):
    """Fill it with results[x]['location']['timezone'] things and types"""


class Coordinates(BaseModel):
    """Fill it with results[x]['location']['coordinates'] things and types"""


class Street(BaseModel):
    """Fill it with results[x]['location']['street'] things and types"""


class Location(BaseModel):
    """Fill it with results[x]['location'] things and types"""


class Name(BaseModel):
    """Fill it with results[x]['name'] things and types"""


class RandomUser(BaseModel):
    """Fill it with results[x] things and types"""


class Info(BaseModel):
    seed: str
    results: int
    page: int
    version = str


class RandomUsers(BaseModel):
    results: RandomUser
    info: Info


if __name__ == "__main__":
    # response = requests.get("https://randomuser.me/api/?results=50")
    # response_json = response.json()
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
    test_output = RandomUser(**test_input)
    assert test_output.name.last == "Mcdonalid"
    assert test_output.location.street.name == "Mockingbird Ln"
    assert test_output.login.username == "crazyduck195"
    assert test_output.registered.age == 3
