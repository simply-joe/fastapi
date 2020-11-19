from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, item: Item):
    return {"item_id": item_id, "q": q, "item_name": item.name}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name}

@app.get("/stores/{store_id}")
def read_store(store_id: int, q: str = None):
    return {"store_id": store_id, "q": q}
