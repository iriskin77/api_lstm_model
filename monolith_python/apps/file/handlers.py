from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, BackgroundTasks
from apps.file import services
from apps.file.schema import FileUpdate, FileFilter, FilesGet, FileGet, FilePost
from apps.user.users.models import User
from apps.user.auth.login import get_current_user_from_token
from fastapi.responses import JSONResponse, FileResponse


router_file = APIRouter()


@router_file.get("/", response_model=FileGet)
async def get_file(id: int, current_user: User = Depends(get_current_user_from_token)):
    """get_file принимает id файла, возвращает файл, принадлежайщий пользователю. Только для авторизованных пользователей"""

    file = await services.get_file_by_id(id=id)

    if file is None:
        raise HTTPException(status_code=404, detail="File with this id was not found")

    try:
        file = await services.get_file_by_id_for_user(id=id, user=current_user)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f'database error {ex}')
    return file


@router_file.get("/files", response_model=FilesGet)
async def get_files_list(current_user: User = Depends(get_current_user_from_token)):
    """Возвращает набор файлов, которые принадлежат пользователю. Только для авторизованных пользователей"""
    try:
        files = await services.get_files_list(user=current_user)
        return {'files': files}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f'database error {ex}')


@router_file.post("/", response_model=FilePost)
async def upload_file(filename: str = Form(...),
                      column: str = Form(...),
                      file: UploadFile = File(...),
                      current_user: User = Depends(get_current_user_from_token)):
    """Позволяет загружать файл на сервер. Только для авторизованных пользователей"""

    try:
        file_id = await services.save_file(user=current_user,
                                           filename=filename,
                                           column=column,
                                           file=file)
        return {'id': file_id}

    except Exception as ex:
        raise HTTPException(status_code=500, detail=f'database error {ex}')


@router_file.patch("/", response_model=FileGet)
async def change_file(id: int,
                      params: FileUpdate,
                      current_user: User = Depends(get_current_user_from_token)):

    """Позволяет менять данные о файле файл. Только для авторизованных пользователей"""

    file = await services.get_file_by_id(id=id)

    if file is None:
        raise HTTPException(status_code=404, detail="File with this id was not found")

    if params == {}:
        raise HTTPException(status_code=404, detail="at least one parametr")

    params_to_update = params.dict(exclude_none=True)
    try:
        file_updated = await services.change_file(id=id, params=params_to_update, user=current_user)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f'database error {ex}')
    return file_updated


@router_file.get("/filter/", response_model=FilesGet)
async def get_filtered_files(params: FileFilter = Depends()):
    if params == {}:
        raise HTTPException(status_code=422,
                            detail="At least one parameter should be provided")

    """Позволяет получить список файлов по заданным критериям"""

    try:
        params_to_filter = params.dict(exclude_none=True)

        files = await services.filter_files(params_to_filter=params_to_filter)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f'database error {ex}')
    return files


@router_file.patch("/process_file")
async def process_file(id: int,
                       background_tasks: BackgroundTasks,
                       current_user: User = Depends(get_current_user_from_token)):

    """Позволяет использовать ML модель и определять тональность текстов в файле. Только для авторизованных пользователей"""

    file = await services.get_file_by_id(id=id)

    if file is None:
        raise HTTPException(status_code=404, detail="File with this id was not found")

    try:
        user_id = current_user.id
        background_tasks.add_task(services.process_comments, id, user_id)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f'database error {ex}')
    return JSONResponse({'success': 200})


@router_file.get("/download_file")
async def download_file(id: int,
                        current_user: User = Depends(get_current_user_from_token)):

    """Позволяет скачивать файл. Только для авторизованных пользователей"""

    content_type_xlsx = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    file = await services.get_file_by_id(id=id)

    if file is None:
        raise HTTPException(status_code=404, detail="File with this id was not found")

    try:
        file = await services.download(id=id, user=current_user)
        return FileResponse(file.file, media_type=content_type_xlsx, filename=file.filename)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f'database error {ex}')
