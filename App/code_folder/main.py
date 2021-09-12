# pip3 install imports
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse
import requests
import pandas as pd

# user created modules
from filter_json import filter_json

app = FastAPI()


@app.get("/get")
async def get_imgw_data():
    response = requests.get("https://danepubliczne.imgw.pl/api/data/synop")
    return JSONResponse(status_code=status.HTTP_200_OK, content=response.json())


@app.get("/get_imgw_with_station_id")
async def get_imgw_with_station_id(station_id: int = 0):
    response = requests.get("https://danepubliczne.imgw.pl/api/data/synop")
    return JSONResponse(status_code=status.HTTP_200_OK, content=filter_json(response.json(), str(station_id)))


@app.get("/get_random_users")
async def get_random_users(how_much: int = 1):
    response = requests.get(f"https://randomuser.me/api/?results={how_much}")
    response_json = response.json()
    # df = pd.DataFrame(response.json()["results"])
    # df.to_excel("Some_excel.xlsx")
    dictio = {"employee1": "employee1_obj", "employee2": "employee2_obj", "employee3": "employee3_obj"}
    return JSONResponse(status_code=status.HTTP_200_OK)


@app.post("/post")
async def post_data(request: Request):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"key": "some value"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
