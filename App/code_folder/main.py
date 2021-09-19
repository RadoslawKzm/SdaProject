# pip3 install imports
import requests
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse

# user created modules
from App.code_folder.employee import Employee
from App.code_folder.filter_json import filter_json

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
    # import pandas as pd
    # df = pd.DataFrame(response.json()["results"])
    # df.to_excel("Some_excel.xlsx")
    Dupa = 1
    print(Dupa)
    return JSONResponse(status_code=status.HTTP_200_OK, content=response.json()["results"])


@app.get("/create_random_users")
async def create_random_users(how_much: int = 1):
    response = requests.get(f"https://randomuser.me/api/?results={how_much}")
    response_json = response.json()
    for person in response_json["results"]:
        name = person["name"]["first"]
        last = person["name"]["last"]
        age = person["dob"]["age"]
        Employee(name=name, last_name=last, age=age)
    # dictio = Employee.registry

    return JSONResponse(status_code=status.HTTP_200_OK, content=Employee.get_json_registry())


@app.post("/post")
async def post_data(request: Request):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"key": "some value"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
