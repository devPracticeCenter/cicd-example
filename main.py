from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def read_root():
    return {"Hello": "World2"}

@app.get("/a")
def read_root():
    return {"Hello": "World aaaaaaaaaaaaa!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}