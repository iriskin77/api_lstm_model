import os
import aiofiles
import random
import string
from fastapi import HTTPException, UploadFile, File, Form
from settings.settings import PATH_FILE_STORAGE
from apps.file.models import FileToUpload


# ============ Insert a file into db ===========


async def save_file(filename: str = Form(...),
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
                            file=filename_path)
    await new_file.save()

    return new_file.id


def generate_random_string():
    letters = string.ascii_letters
    rand_string = ''.join(random.choice(letters) for i in range(8))
    return rand_string


async def get_file_by_id(id: int):
    file_check = await FileToUpload.filter(id=id).exists()
    if file_check:
        file = await FileToUpload.filter(id=id).first()
        return file


async def get_files_list():
    files = await FileToUpload.all()
    return files


async def change_file(id: int, params):
    file = await FileToUpload.filter(id=id).first()
    await file.update_from_dict(params).save()
    return file.id


async def filter_files(params_to_filter):
    files = await FileToUpload.filter(**params_to_filter)
    return files


async def delete_file_by_id(id: int):
    pass
