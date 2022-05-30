import os

import requests
from typing import Union
from fastapi import FastAPI, Header

app = FastAPI()


@app.post("/")
def create_order(authorization: Union[str, None] = Header(default=None)):
    authorization = str.replace(authorization, "Bearer ", "")
    response = requests.get(os.getenv("TALARON_URI")+"/validate/"+authorization)
    if response.json()["success"]:
        return response.json()
    else:
        return response.json()