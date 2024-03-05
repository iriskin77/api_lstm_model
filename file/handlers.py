from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from . import services
from .schema import FilePost, FileGet, FileUpdate, FileFilter
from models.models import Test_Pydantic_Response


router = APIRouter()


@router.get("/")
async def get_file(id: int):

    try:
        file = await services.get_file_by_id(id=id)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f'database error {ex}')
    else:
        if file is not None:
            return file
        raise HTTPException(status_code=404, detail="File with this id was not found")


@router.get("/files")
async def get_files_list():
    try:
        files = await services.get_files_list()
        return files
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f'database error {ex}')


@router.post("/")
async def upload_file(filename: str = Form(...),
                      column: str = Form(...),
                      file: UploadFile = File(...)):

    try:
        file_id = await services.save_file(filename=filename, column=column, file=file)
        return file_id

    except Exception as ex:
        raise HTTPException(status_code=500, detail=f'database error {ex}')


@router.patch("/")
async def change_file(id: int, params: FileUpdate):
    file = await services.get_file_by_id(id=id)

    if file is None:
        raise HTTPException(status_code=404, detail="File with this id was not found")

    if params == {}:
        raise HTTPException(status_code=404, detail="at least one parametr")

    params_to_update = params.dict(exclude_none=True)

    file_updated = await services.change_file(id=id, params=params_to_update)

    return file_updated


@router.get("/filter/{params}")
async def get_filtered_files(params: FileFilter = Depends()):
    if params == {}:
        raise HTTPException(status_code=422,
                            detail="At least one parameter should be provided")

    params_to_filter = params.dict(exclude_none=True)

    res = await services.filter_files(params_to_filter=params_to_filter)
    return res
