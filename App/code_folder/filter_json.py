import pickle
from typing import List, Dict


def filter_json(_json: List[Dict], id_stacji: str) -> Dict:
    """Given list in _json variable return a dict that contains {id_stacji: {whole dict for given station}}"""
    # dict_1 = {}
    # for item in _json:
    #     dict_1[item["id_stacji"]] = item
    # dict_1 = dict_1[id_stacji]
    print(f"{__name__ = }")
    return {item["id_stacji"]: item for item in _json}[id_stacji]


# if __name__ == "__main__":
with open("json.pickle", "rb") as file:
    our_json = pickle.load(file)
output = filter_json(_json=our_json, id_stacji="12650")
print(f"\n\n{'*'*30}\n\ndupa\n\n{'*'*30}\n\n")
