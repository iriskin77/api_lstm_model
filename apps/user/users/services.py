from datetime import datetime
from typing import Union

from apps.user.users.models import User
from fastapi import HTTPException


async def create_user(name: str, surname: str, email: str, hashed_password: str):
    try:
        new_user = await User(
            name=name,
            surname=surname,
            email=email,
            created_at=datetime.now(),
            hashed_password=hashed_password,
        )
        await new_user.save()
        return new_user.id

    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


async def get_user_by_email(email: str):
    user = User.filter(email=email).exists()
    if user:
        user_by_email = User.filter(email=email).first()
        return user_by_email

