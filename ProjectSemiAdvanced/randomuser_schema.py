from typing import Optional

from pydantic import BaseModel


class Dob(BaseModel):
    date: str
    age: int


class RandomUser(BaseModel):
    gender: Optional[str]
    name: dict
    location: dict
    email: str
    login: dict
    dob: Dob
    registered: dict
    phone: str
    cell: str
    id: dict
    picture: dict
    nat: str
