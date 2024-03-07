from datetime import timedelta
from typing import Union
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from jose import JWTError
from settings import settings
from .schema import Token
from user.users.models import User
from .hash_pass import Hasher
from .security import create_access_token
from user.users import services

router_login = APIRouter()


async def _get_user_by_email_for_auth(email: str):
    return await services.get_user_by_email(email=email)


async def authenticate_user(email: str, password: str) -> Union[User, None]:
    user = await _get_user_by_email_for_auth(email=email)
    print(user)
    if user is None:
        return
    if not Hasher.verify_password(password, user.hashed_password):
        return
    return user


@router_login.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password",)

    # Если пользователь найден по почте, то создаем для него токен
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user.email, "other_custom_data": [1, 2, 3, 4]},
        expires_delta=access_token_expires,
    )

    return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")


async def get_current_user_from_token(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        email: str = payload.get("sub")
        print("username/email extracted is ", email)
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await _get_user_by_email_for_auth(email=email)

    if user is None:
        raise credentials_exception
    return user
