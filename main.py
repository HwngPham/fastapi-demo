from typing import Union
from os import environ
from fastapi import FastAPI
from dotenv import load_dotenv


load_dotenv()


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Worlddddd"}
