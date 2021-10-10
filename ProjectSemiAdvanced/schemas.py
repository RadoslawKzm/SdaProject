from typing import List, Union, Optional

from pydantic import BaseModel

"""Create python model representation of randomuser output using pydantic model"""


class Picture(BaseModel):
    """Fill it with results[x]['picture'] things and types"""
    large: str
    medium: str
    thumbnail: str


class Id(BaseModel):
    """Fill it with results[x]['id'] things and types"""
    name: Optional[str]
    value: Union[str, None]


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
    postcode: Union[int, str]
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
    version: str


class RandomUsers(BaseModel):
    results: List[RandomUser]
    info: Info


class OurUser(BaseModel):
    GENDER: str
    FIRST_NAME: str
    LAST_NAME: str
    EMAIL: str
    AGE: int
    BIRTHDAY: str
    NATIONALITY: str
    LOGIN: str
    PASSWORD: str
    CITY: str
    STREET: str
    NUMBER: int
    COUNTRY: str


class OurUsers(BaseModel):
    data: List[OurUser]
