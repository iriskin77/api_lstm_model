from fastapi import APIRouter
from apps.file import handlers

routes = APIRouter()


routes.include_router(router=handlers.router, prefix="/file")
