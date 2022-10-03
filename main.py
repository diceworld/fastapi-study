from datetime import datetime
from typing import Optional

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Optional[str] = None


@app.put("/items/{id}")
async def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    return fake_db[id]
