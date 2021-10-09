# pip3 install imports
import json
from typing import Dict

import numpy as np
import pandas as pd
from pydantic import BaseModel
import requests

# response = requests.get(url="https://randomuser.me/api/?results=50")
# output = response.json()
# with open("randomuser.json", "w") as file:
#     json.dump(output, file)

with open("randomuser.json", "r") as file:
    output = json.load(file)

df = pd.read_json("randomuser.json")


class RandomUser(BaseModel):
    gender: str
    name: dict
    location: dict
    email: str
    login: dict
    dob: dict
    registered: dict
    phone: str
    cell: str
    id: dict
    picture: dict
    nat: str


# tst: Dict = output[0]
# tst['gender'] = 1
# dupa = RandomUser(**output[0])

requests.post("http://127.0.0.1:8000", json=output[0])