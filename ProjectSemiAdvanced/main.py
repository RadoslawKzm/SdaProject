# pip3 install imports
import json
import numpy as np
import pandas as pd
import requests

# response = requests.get(url="https://randomuser.me/api/?results=50")
# output = response.json()
# with open("randomuser.json", "w") as file:
#     json.dump(output, file)

with open("randomuser.json", "r") as file:
    output = json.load(file)

df = pd.read_json("randomuser.json")

print("pass")