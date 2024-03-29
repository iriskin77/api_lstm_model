from fastapi import APIRouter
import apps.file.handlers as file_handler
import apps.user.users.handlers as user_handler
import apps.user.auth.login as login_handler

routes = APIRouter()


routes.include_router(router=file_handler.router_file, prefix="/file")
routes.include_router(router=user_handler.router_user, prefix="/users")
routes.include_router(router=login_handler.router_login, prefix="/login")
