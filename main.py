from typing import Optional

from fastapi import FastAPI, Cookie, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
        ads_id: Optional[str] = Cookie(default=None),
        user_agent: Optional[str] = Header(default=None)
):
    return {"ads_id": ads_id, "user_agent": user_agent}
