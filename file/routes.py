from fastapi import APIRouter
from file import handlers

routes = APIRouter()


routes.include_router(router=handlers.router, prefix="/file")
