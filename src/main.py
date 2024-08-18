from fastapi import FastAPI
from src.config import settings

app = FastAPI()


@app.get("/")
def home():
    return {"hello": "world"}


@app.get("/{id}")
def getById(id):
    return {"id": settings.ENV}
