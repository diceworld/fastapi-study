from typing import Optional, List

from fastapi import FastAPI
from pydantic import EmailStr
from pydantic.main import BaseModel

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


@app.post("/usr/", response_model=UserOut)
async def create_user(user: UserIn):
    return user
