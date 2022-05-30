from typing import Union
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/")
def read_root(authorization: Union[str, None] = Header(default=None)):
    return {"Token": authorization}