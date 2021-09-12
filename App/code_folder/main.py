# pip3 install imports
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse
import requests

app = FastAPI()


def filter_json(_json: list[dict], id_stacji: int) -> dict[int:dict]:
    pass


@app.get("/get")
async def get_data():
    response = requests.get("https://danepubliczne.imgw.pl/api/data/synop")
    json = response.json()
    station = json[10]
    dictio = {}  # {12650:{'id_stacji': {'12650', 'stacja': 'Kasprowy Wierch', 'data_pomiaru': '2021-09-12', 'godzina_pomiaru': '8', 'temperatura': '9.2', 'predkosc_wiatru': '2', 'kierunek_wiatru': '60', 'wilgotnosc_wzgledna': '67.6', 'suma_opadu': '0', 'cisnienie': None}}
    return JSONResponse(status_code=status.HTTP_200_OK, content=station)


@app.get("/get_params")
async def get_with_params(skip: int = 0, limit: int = 10):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"key": "some value"})


@app.post("/post")
async def post_data(request: Request):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"key": "some value"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
