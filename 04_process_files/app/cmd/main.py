from fastapi import FastAPI
from app.file_process.api.handlers import router

app = FastAPI()

app.include_router(router)




