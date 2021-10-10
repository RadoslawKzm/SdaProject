import pandas as pd
import requests
from fastapi import FastAPI, status, Depends
from fastapi.responses import JSONResponse, FileResponse
from sqlalchemy.orm import sessionmaker, Session

from ProjectSemiAdvanced.schemas import RandomUsers, OurUser, OurUsers
from ProjectSemiAdvanced.db_connector import DbContext, Base, get_db
from ProjectSemiAdvanced.models import BaseTable
from ProjectSemiAdvanced.user_extractor import exctractor

app = FastAPI()


@app.on_event("startup")
async def create_database_structures():
    Base.metadata.create_all(DbContext.get_engine())


@app.get("/")
async def get_random_user(how_much: int = 1):
    response = requests.get(f"https://randomuser.me/api/?results={how_much}").json()
    users = RandomUsers(**response)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data": users.dict()})


@app.post("/users")
async def populate_db_with_users(how_much: int = 1):
    response = requests.get(f"https://randomuser.me/api/?results={how_much}").json()
    Session = sessionmaker(bind=DbContext.get_engine())
    session = Session()
    for dictio in response["results"]:
        user = exctractor(input_dict=dictio)
        session.add(BaseTable(**user))
    session.commit()
    session.close()
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"data": f"{how_much} users created in DB"})


@app.get("/users", response_model=OurUsers)
async def get_all_users():
    with DbContext(suppress=False, bind=DbContext.get_engine()) as session:
        users = [OurUser(**user.__dict__).dict() for user in session.query(BaseTable).all()]
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data": users})


@app.get("/users/csv")
async def get_users_csv(session: Session = Depends(get_db)):
    users = [OurUser(**user.__dict__).dict() for user in session.query(BaseTable).all()]
    df = pd.DataFrame(users)
    df.to_csv("response.csv")
    return FileResponse(path="response.csv",
                        status_code=status.HTTP_200_OK,
                        filename="users.csv")


@app.get("/users/excel")
async def get_users_csv():
    Session = sessionmaker(bind=DbContext.get_engine())
    session = Session()
    users = [OurUser(**user.__dict__).dict() for user in session.query(BaseTable).all()]
    session.close()
    df = pd.DataFrame(users)
    df.to_excel("response.xlsx")
    return FileResponse(path="response.xlsx",
                        status_code=status.HTTP_200_OK,
                        filename="users.xlsx")


@app.get("/users/json")
async def get_users_csv():
    Session = sessionmaker(bind=DbContext.get_engine())
    session = Session()
    users = [OurUser(**user.__dict__).dict() for user in session.query(BaseTable).all()]
    session.close()
    df = pd.DataFrame(users)
    df.to_json("response.json")
    return FileResponse(path="response.json",
                        status_code=status.HTTP_200_OK,
                        filename="users.json")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
