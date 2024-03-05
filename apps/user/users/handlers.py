from fastapi import APIRouter, Depends, HTTPException
from . import services
from .schema import UserCreate
from apps.user.auth.hash_pass import Hasher


router_user = APIRouter()


@router_user.post("/")
async def user_create(item: UserCreate):
    try:
        new_user = await services.create_user(
            name=item.name,
            surname=item.surname,
            email=item.email,
            hashed_password=Hasher.get_password_hash(item.password),
        )

        return new_user

    except Exception as ex:
        HTTPException(status_code=503, detail=f"Database error: {ex}")


