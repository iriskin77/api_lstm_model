from fastapi import APIRouter
# import apps.file.handlers as file_handler
# import apps.user.users.handlers as user_handler
# import apps.user.auth.login as login_handler
from .file.handlers import router_file
from .user.users.handlers import router_user
from .user.auth.login import router_login


routes = APIRouter()

routes.include_router(router=router_file, prefix="/file")
routes.include_router(router=router_user, prefix="/users")
routes.include_router(router=router_login, prefix="/login")
