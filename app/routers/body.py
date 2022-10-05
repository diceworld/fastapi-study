from typing import Optional, List

from fastapi import APIRouter, Body
from pydantic import BaseModel, Field, HttpUrl

router = APIRouter(
    prefix="/body",
    tags=["body"],
)


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(default=None, title="description", max_length=30)


@router.put("/{item_id}")
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


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item2(BaseModel):
    name: str
    description: Optional[str] = Field(default=None, title="description", max_length=30)
    tags: List[str] = []
    image: Optional[List[Image]] = None


@router.put("/v2/{item_id}")
async def update_item2(
        *,
        item_id: int,
        item: Item2 = Body(embed=True)
):
    results = {"item_id": item_id, "item": item}

    return results
