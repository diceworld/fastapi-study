import uuid
from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Body, Cookie, Header, status, File, UploadFile, Form

router = APIRouter(
    prefix="/extra",
    tags=["extra"],
)


@router.get("/uuid")
async def get_uuid():
    return {
        "uuid": uuid.uuid1(),
    }


@router.put("/{item_id}")
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


@router.get("/cookie/")
async def read_cookie(
        ads_id: Optional[str] = Cookie(default=None),
        user_agent: Optional[str] = Header(default=None)
):
    return {"ads_id": ads_id, "user_agent": user_agent}


@router.post("/status-code/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}


@router.post("/files/")
async def create_file(
        file: bytes = File(), fileb: UploadFile = File(), token: str = Form()
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
