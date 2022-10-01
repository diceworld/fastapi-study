from typing import Optional, Union, List

from fastapi import FastAPI, Query
from pydantic import Required

app = FastAPI()


@app.get("/item/")
async def read_item(q: Optional[str] = Query(default=Required, min_length=3, max_length=50, regex="[a-zA-Z]")):
    results = {"item": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update({"q": q})

    return results


@app.get("/items/")
async def read_items(q: Union[List[str], None] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items


@app.get("/goods/")
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
