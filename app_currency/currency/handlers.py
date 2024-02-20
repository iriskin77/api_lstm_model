from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession
from . import db
from core.async_session import get_async_session
from .schema import FilePost, FileGet


router = APIRouter()


@router.get("/", response_model=FileGet)
async def get_file(id: int, async_session: AsyncSession = Depends(get_async_session)):
    file = await db.get_file_by_id(id=id, async_session=async_session)
    if file is not None:
        return file


@router.post("/", response_model=FilePost)
async def upload_file(column: str = Form(...),
                      file: UploadFile = File(...),
                      async_session: AsyncSession = Depends(get_async_session)):

    new_file = await db.save_file(column=column,
                                  file=file,
                                  async_session=async_session)

    return new_file

