import re
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

    # @field_validator('password', mode='before')
    # @classmethod
    # def check_password(cls, value):
    #     pattern_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    #     if re.match(pattern_password, value) is not None:
    #         return value
    #
    # @field_validator('email', mode='before')
    # @classmethod
    # def check_email(cls, value):
    #     pattern_email = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
    #     if re.match(pattern_email, value) is not None:
    #         return value


class UserUpdate(UserBase):
    name: Optional[str]
    surname: Optional[str]
    email: Optional[str]
    password: Optional[str]
