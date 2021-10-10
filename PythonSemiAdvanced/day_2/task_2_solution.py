# built-in imports
from typing import Dict, List

# pip3 imports
import requests
from pydantic import BaseModel

"""Create python model representation of randomuser output using pydantic model"""


class Picture(BaseModel):
    """Fill it with results[x]['picture'] things and types"""
    large: str
    medium: str
    thumbnail: str


class Id(BaseModel):
    """Fill it with results[x]['id'] things and types"""
    name: str
    value: str


class Registered(BaseModel):
    """Fill it with results[x]['registered'] things and types"""
    date: str
    age: int


class Dob(BaseModel):
    """Fill it with results[x]['dob'] things and types"""
    date: str
    age: int


class Login(BaseModel):
    """Fill it with results[x]['login'] things and types"""
    uuid: str
    username: str
    password: str
    salt: str
    md5: str
    sha1: str
    sha256: str


class Timezone(BaseModel):
    """Fill it with results[x]['location']['timezone'] things and types"""
    offset: str
    description: str


class Coordinates(BaseModel):
    """Fill it with results[x]['location']['coordinates'] things and types"""
    latitude: str
    longitude: str


class Street(BaseModel):
    """Fill it with results[x]['location']['street'] things and types"""
    number: int
    name: str


class Location(BaseModel):
    """Fill it with results[x]['location'] things and types"""
    street: Street
    city: str
    state: str
    country: str
    postcode: int
    coordinates: Coordinates
    timezone: Timezone


class Name(BaseModel):
    """Fill it with results[x]['name'] things and types"""
    title: str
    first: str
    last: str


class RandomUser(BaseModel):
    """Fill it with results[x] things and types"""
    gender: str
    name: Name
    location: Location
    email: str
    login: Login
    dob: Dob
    registered: Registered
    phone: str
    cell: str
    id: Id
    picture: Picture
    nat: str


class Info(BaseModel):
    seed: str
    results: int
    page: int
    version : str


class RandomUsers(BaseModel):
    results: List[RandomUser]
    info: Info


if __name__ == "__main__":
    # response = requests.get("https://randomuser.me/api/?results=50")
    # response_json = response.json()
    test_input = {"results": [{
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
    }],
        "info": {'seed': '8ff3f93aca4f1084', 'results': 50, 'page': 1, 'version': '1.3'}}
    test_output = RandomUsers(**test_input)
    assert test_output.results[0].name.last == "Mcdonalid"
    assert test_output.results[0].location.street.name == "Mockingbird Ln"
    assert test_output.results[0].login.username == "crazyduck195"
    assert test_output.results[0].registered.age == 3
