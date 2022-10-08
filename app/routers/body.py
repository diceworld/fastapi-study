from typing import Optional, List, Union

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
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


class Item3(BaseModel):
    name: Optional[str] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@router.get("/v3/{item_id}", response_model=Item3)
async def read_item(item_id: str):
    return items[item_id]


@router.put("/v3/{item_id}", response_model=Item3)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded
