# pip3 install imports
from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse
import requests

# user created modules
from filter_json import filter_json

app = FastAPI()


@app.get("/get")
async def get_data():
    response = requests.get("https://danepubliczne.imgw.pl/api/data/synop")
    json = response.json()
    dictio = filter_json(json, "12650")
    return JSONResponse(status_code=status.HTTP_200_OK, content=dictio)


@app.get("/get_params")
async def get_with_params(skip: int = 0, limit: int = 10):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"key": "some value"})


@app.post("/post")
async def post_data(request: Request):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"key": "some value"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
