from fastapi import FastAPI, Request
from randomuser_schema import RandomUser

app = FastAPI()


@app.post("/")
async def do_something(request: RandomUser):
    # response = await request.json()
    print("pass")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
