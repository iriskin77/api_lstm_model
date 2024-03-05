from fastapi import HTTPException
from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional


# ==============User Request models =============

class UserBase(BaseModel):
    name: str
    surname: str
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    name: Optional[str]
    surname: Optional[str]
    email: Optional[str]
    password: Optional[str]
