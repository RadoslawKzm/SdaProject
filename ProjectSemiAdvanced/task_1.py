"""
1. load randomuser.json
2. delete every dict for each user in json
3. create dataframe from unnested data
4. save as new json and csv
"""
import json
import pandas as pd

with open("randomuser.json") as file:
    data = json.load(file)

new_list2 = [{key: value for key, value in sub_dict.items() if type(value) != dict} for sub_dict in data]
df = pd.DataFrame(new_list2)
df.to_csv("test.csv")
df.to_json("test.json")
