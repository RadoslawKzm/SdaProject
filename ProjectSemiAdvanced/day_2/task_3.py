import requests
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from ProjectSemiAdvanced.day_2.task_2 import RandomUsers


async def get_user():
    """
    Create get API endpoint under '/' link at 127.0.0.1:8000 host.
    This api will call randomuser API and get 1 user.
    Our code will parse incoming request using our RandomUsers model
    Our API will return status code=200 and json.
    json={"first_name"="Marek", "last_name":"Mostowiak", "age":69, "email":"mareczq69@gmail.com"}
    """
    # response = requests.get("https://randomuser.me/api/?results=1")
    # response_json = response.json()
    # random_users = RandomUsers(**response_json)
    return JSONResponse(status_code="dupa", content={"dupa nie content": 69})
