import uuid
from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID

from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/uuid")
async def get_uuid():
    return {
        "uuid": uuid.uuid1(),
    }


@app.put("/items/{item_id}")
async def read_items(
        item_id: UUID,
        start_datetime: Optional[datetime] = Body(default=None),
        end_datetime: Optional[datetime] = Body(default=None),
        repeat_at: Optional[time] = Body(default=None),
        process_after: Optional[timedelta] = Body(default=None)
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process

    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "precess_after": process_after,
        "start_process": start_process,
        "duration": duration
    }
