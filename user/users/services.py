from datetime import datetime
from typing import Union

from tortoise.expressions import Q

from user.users.models import User
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
    user = await User.filter(email=email).exists()
    print("get_user_by_email", user)
    if user:
        user_by_email = await User.filter(email=email).first()
        return user_by_email


async def get_user_by_id(id: int):
    user = await User.filter(id=id).exists()
    if user:
        user_by_id = await User.filter(id=id).first()
        return user_by_id


async def get_auth_user_by_id(id: int, user: User):
    _user = await get_user_by_id(id=id)
    if _user.id == user.id:
        return _user


async def update_user(id: int, params_to_update: dict, user: User):
    user_to_update = await get_auth_user_by_id(id=id, user=user)
    if user_to_update is not None:
        await user_to_update.update_from_dict(params_to_update).save()
        return user_to_update


async def delete_user(id: int, user: User):
    user_to_delete = await get_auth_user_by_id(id=id, user=user)
    if user_to_delete is not None:
        await user_to_delete.delete()
        return user_to_delete.id
