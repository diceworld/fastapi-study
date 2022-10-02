from typing import Optional, List

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


class Item2(BaseModel):
    name: str = Field(example="Foo")
    description: Optional[str] = Field(default=None, example="A very nice Item")
    price: float = Field(example=35.4)
    tax: Optional[float] = Field(default=None, example=3.2)


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, item2: Item2):
    results = {"item_id": item_id, "item": item, "item2": item2}

    return results
