from fastapi import APIRouter, Depends, HTTPException
from . import services
from .schema import UserBase, UserCreate, UserUpdate
from apps.user.auth.hash_pass import Hasher
from apps.user.auth.login import get_current_user_from_token
from .models import User


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


@router_user.get("/")
async def get_user(id: int, current_user: User = Depends(get_current_user_from_token)):
    try:
        user = await services.get_auth_user_by_id(id=id, user=current_user)
        return user
    except Exception as ex:
        HTTPException(status_code=503, detail=f"Database error: {ex}")


@router_user.patch("/")
async def update_user(id: int, item: UserUpdate, current_user: User = Depends(get_current_user_from_token)):
    params_to_update = item.dict(exclude_none=True)
    if params_to_update == {}:
        raise HTTPException(status_code=422, detail="At least one parameter for user update info should be provided")

    user = await services.get_user_by_id(id=id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found.")

    #check_perm = db_user.check_user_permissions(target_user=user, current_user=current_user)

    try:
        updated_user_id = await services.update_user(id=id,
                                                     params_to_update=params_to_update,
                                                     user=user)
        return updated_user_id
    except Exception as ex:
        HTTPException(status_code=503, detail=f"Database error: {ex}")


@router_user.delete("/")
async def user_delete(id: int, current_user: User = Depends(get_current_user_from_token)):

    user = await services.get_user_by_id(id=id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found.")

    #check_perm = db_user.check_user_permissions(target_user=user, current_user=current_user)

    try:
        deleted_user_id = await services.delete_user(id=id, user=user)
        return deleted_user_id
    except Exception as ex:
        raise HTTPException(status_code=503, detail=f"Database error: {ex}")
