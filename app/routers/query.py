from typing import Optional, Union, List

from fastapi import APIRouter, Query, Path
from pydantic import Required

router = APIRouter(
    prefix="/query",
    tags=["query"],
)


@router.get("/item/")
async def read_item(q: Optional[str] = Query(default=Required, min_length=3, max_length=50, regex="[a-zA-Z]")):
    results = {"item": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update({"q": q})

    return results


@router.get("/items/")
async def read_items(q: Union[List[str], None] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items


@router.get("/goods/")
async def read_goods(
        q: Optional[str] = Query(
            default=None,
            alias="goods-query",
            title="Query string",
            description="Query String for the items to search in the database that have a good match",
            min_length=3,
        )
):
    results = {"goods": [{"goods_id": "foo"}, {"goods_id": "bar"}]}

    if q:
        results.update({"q": q})

    return results


@router.get("/items/{item_id}")
async def read_items(
        *, item_id: int = Path(title="The ID of the item to get", gt=0, le=1000),
        q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})

    return results
