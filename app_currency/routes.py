from fastapi import APIRouter
from currency import handlers

routes = APIRouter()


routes.include_router(router=handlers.router, prefix="/currency")
