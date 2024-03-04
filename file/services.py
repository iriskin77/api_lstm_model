


# ============ Insert a file into db ===========


# async def save_file(async_session: AsyncSession,
#                     column: str = Form(...),
#                     file: UploadFile = File(...)):
#
#     if not os.path.isdir(path_file_storage):
#         os.mkdir(path_file_storage)
#
#     if file.content_type != "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
#         raise HTTPException(status_code=500, detail="Content-type should be xlsx")
#
#     # есть ли файл с таким именем
#     if os.path.isfile(path_file_storage + file.filename):
#         rand_str = generate_random_string()
#         filename = path_file_storage + f"{rand_str}_{file.filename}"
#     else:
#         filename = path_file_storage + file.filename
#
#     async with aiofiles.open(filename, "wb") as buffer:
#         data = await file.read()
#         await buffer.write(data)
#
#     new_file = FileUpload(name=file.filename, column=column, file=filename)
#     async_session.add(new_file)
#     await async_session.commit()
#
#     res = {'name': file.filename, 'column': column, 'file': filename}
#
#     return res


# def generate_random_string():
#     letters = string.ascii_letters
#     rand_string = ''.join(random.choice(letters) for i in range(8))
#     return rand_string
#
#
# async def get_file_by_id(id: int, async_session: AsyncSession):
#     query = select(FileUpload).where(FileUpload.id == id)
#     file = await async_session.execute(query)
#     file_row = file.fetchone()
#     if file_row is not None:
#         return file_row[0]
