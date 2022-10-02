from typing import Optional, List

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(default=None, title="description", max_length=30)
    tags: List[str] = []
    image: Optional[List[Image]] = None


@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int,
        item: Item = Body(embed=True)
):
    results = {"item_id": item_id, "item": item}

    return results
