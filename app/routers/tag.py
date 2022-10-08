from enum import Enum
from typing import Union, Set

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/tag",
    tags=["tag"],
)


class Tags(Enum):
    items = "items"
    users = "users"


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


@router.post(
    "/items/",
    response_model=Item,
    summary="Create an item",
    tags=[Tags.items]
)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


@router.get("/users/", tags=[Tags.users])
async def read_users():
    return ["Rick", "Morty"]
