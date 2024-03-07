from fastapi import APIRouter, Depends, HTTPException
from . import services
from .schema import UserCreate, UserUpdate, UserId, UserGet
from user.auth.hash_pass import Hasher
from user.auth.login import get_current_user_from_token
from .models import User


router_user = APIRouter()


@router_user.post("/", response_model=UserId)
async def user_create(item: UserCreate):
    try:
        new_user_id = await services.create_user(
            name=item.name,
            surname=item.surname,
            email=item.email,
            hashed_password=Hasher.get_password_hash(item.password),
        )

        return {'id': new_user_id}

    except Exception as ex:
        HTTPException(status_code=503, detail=f"Database error: {ex}")


@router_user.get("/", response_model=UserGet)
async def get_user(id: int, current_user: User = Depends(get_current_user_from_token)):

    try:
        user = await services.get_user_by_id(id=id)
    except Exception as ex:
        HTTPException(status_code=503, detail=f"Database error: {ex}")
    else:
        if user is None:
            raise HTTPException(status_code=404, detail=f"User with id {id} not found.")
        return user


@router_user.patch("/", response_model=UserGet)
async def update_user(id: int, item: UserUpdate, current_user: User = Depends(get_current_user_from_token)):

    params_to_update = item.dict(exclude_none=True)
    if params_to_update == {}:
        raise HTTPException(status_code=422, detail="At least one parameter for user update info should be provided")

    user = await services.get_user_by_id(id=id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found.")

    try:
        updated_user = await services.update_user(id=id,
                                                  params_to_update=params_to_update,
                                                  user=current_user)

        if updated_user is not None:
            return updated_user
        raise HTTPException(status_code=403, detail=f"You have no permission to update other users")
    except Exception as ex:
        HTTPException(status_code=503, detail=f"Database error: {ex}")


@router_user.delete("/", response_model=UserId)
async def user_delete(id: int, current_user: User = Depends(get_current_user_from_token)):

    user = await services.get_user_by_id(id=id)
    if user is None:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found.")

    try:
        deleted_user_id = await services.delete_user(id=id, user=current_user)
        if deleted_user_id is not None:
            return {'id': deleted_user_id}
        raise HTTPException(status_code=403, detail=f"You have no permission to update other users")
    except Exception as ex:
        raise HTTPException(status_code=503, detail=f"Database error: {ex}")
