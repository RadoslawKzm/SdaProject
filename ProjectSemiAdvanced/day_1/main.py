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

df = pd.DataFrame([user])
df.to_json("test.json")
df.to_csv("test.csv")
df.to_excel("test.xlsx")
