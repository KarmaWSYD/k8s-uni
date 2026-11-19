from fastapi import FastAPI, Request

app = FastAPI()

@app.get(path="/")
async def index(request: Request):
    return 200