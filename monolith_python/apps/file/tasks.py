from datetime import datetime
from tortoise.expressions import Q
from apps.file.models import FileToUpload
from apps.file.lstm_model.lstm_model import process_file_data


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

