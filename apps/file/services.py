import os
import aiofiles
import random
import string
from fastapi import HTTPException, UploadFile, File, Form
from settings.settings import PATH_FILE_STORAGE
from apps.user.users.models import User
from datetime import datetime
from tortoise.expressions import Q
from apps.file.models import FileToUpload
from apps.file.lstm_model.lstm_model import process_file_data

# ============ Insert a file into db ===========


async def save_file(user: User,
                    filename: str = Form(...),
                    column: str = Form(...),
                    file: UploadFile = File(...)) -> int:

    if not os.path.isdir(PATH_FILE_STORAGE):
        os.mkdir(PATH_FILE_STORAGE)

    xlsx_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    if file.content_type != xlsx_type:
        raise HTTPException(status_code=500, detail="Content-type should be xlsx")

    # есть ли файл с таким именем
    if os.path.isfile(PATH_FILE_STORAGE + file.filename):
        rand_str = generate_random_string()
        filename_path = PATH_FILE_STORAGE + f"{rand_str}_{file.filename}"
    else:
        filename_path = PATH_FILE_STORAGE + file.filename

    async with aiofiles.open(filename_path, "wb") as buffer:
        data = await file.read()
        await buffer.write(data)

    new_file = FileToUpload(filename=filename,
                            column=column,
                            file=filename_path,
                            user=user)
    await new_file.save()

    return new_file.id


def generate_random_string():
    letters = string.ascii_letters
    rand_string = ''.join(random.choice(letters) for i in range(8))
    return rand_string


async def get_file_by_id_for_user(id: int, user: User):
    file = await FileToUpload.filter(Q(id=id) & Q(user=user.id)).first()
    return file


async def get_file_by_id(id: int):
    file_check = await FileToUpload.filter(id=id).exists()
    if file_check:
        file = await FileToUpload.filter(id=id).first()
        return file


async def get_files_list():
    files = await FileToUpload.all()
    return files


async def change_file(id: int, params, user: User):
    file = await FileToUpload.filter(Q(id=id) & Q(user=user.id)).first()
    await file.update_from_dict(params).save()
    return file.id


async def filter_files(params_to_filter):
    files = await FileToUpload.filter(**params_to_filter)
    return files


async def delete_file_by_id(id: int):
    file = await get_file_by_id(id=id)
    await file.delete()
    return file.id


async def process_comments(file_id, user_id):
    file = await FileToUpload.filter(Q(id=file_id) & Q(user=user_id)).first()
    file_path = file.file
    file_column = file.column
    file.is_processing = True
    await file.save()

    try:
        process_file_data(file_path=file_path, name_column=file_column)
    except Exception as ex:
        print(ex)
    else:
        file.is_processed = True
        file.processed_at = datetime.now()
        file.is_processing = False
        await file.save()
