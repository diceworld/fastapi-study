from typing import Union

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(
        q: Union[str, None] = None,
        skip: int = 0,
        limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}


class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: CommonQueryParams = Depends(CommonQueryParams)):
    return commons
