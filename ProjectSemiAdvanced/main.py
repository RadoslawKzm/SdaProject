# pip3 install imports
import json
from typing import Dict

import numpy as np
import pandas as pd

import requests

user = {
    "gender": "female",
    "name": "Hana",
    "last": "Meunier",
    "city": "Jussy",
    "country": "Switzerland",
    "postcode": 2572}


df = pd.DataFrame(user.items())

# response = requests.get(url="https://randomuser.me/api/?results=50")
# output = response.json()
# with open("randomuser.json", "w") as file:
#     json.dump(output, file)
#
# with open("randomuser.json", "r") as file:
#     output = json.load(file)
#
# df = pd.read_json("randomuser.json")


# tst: Dict = output[0]
# tst['gender'] = 1
# dupa = RandomUser(**output[0])

# del output[0]['gender']
# response = requests.post("http://127.0.0.1:8000", json=output[0])
