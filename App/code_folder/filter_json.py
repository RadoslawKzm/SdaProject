import pickle

with open("json.pickle", "rb") as file:
    our_json = pickle.load(file)


def filter_json(_json: list[dict], id_stacji: int) -> dict[int:dict]:
    print(f"{id_stacji = }")
    print(_json)


filter_json(_json=our_json, id_stacji=12650)
