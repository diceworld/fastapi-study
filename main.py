from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(default=None, title="description", max_length=30)


@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int,
        item: Item = Body(embed=True),
        q: Optional[str] = None
):
    results = {"item_id": item_id, "item": item}

    if q:
        results.update({"q": q})

    return results
