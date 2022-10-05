from enum import Enum

from fastapi import APIRouter

router = APIRouter(
    prefix="/enum",
    tags=["enum"],
)


class ModelName(str, Enum):
    test1 = "test1"
    test2 = "test2"
    test3 = "test3"


@router.get("/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@router.get("/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.test1:
        return {"model_name": model_name, "message": "test1 model"}

    if model_name is ModelName.test2:
        return {"model_name": model_name, "message": "test2 model"}

    return {"model_name": model_name, "message": "test3 model"}
