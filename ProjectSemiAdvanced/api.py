from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/")
def do_something(request: Request):
    print("pass")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
