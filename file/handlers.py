from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from . import services
from .schema import FilePost, FileGet


router = APIRouter()


@router.get("/", response_model=FileGet)
async def get_file(id: int):

    try:
        pass
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f'database error {ex}')


@router.post("/", response_model=FilePost)
async def upload_file(column: str = Form(...),
                      file: UploadFile = File(...)):

    try:
        pass

    except Exception as ex:
        raise HTTPException(status_code=500, detail=f'database error {ex}')

