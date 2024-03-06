from datetime import datetime
from apps.file.models import FileToUpload
from apps.worker import celery
from apps.file import services
from apps.file.lstm_model.lstm_model import process_file_data


@celery.task(bind=True)
async def process_comments(self, file_id):
    file = await services.get_file_by_id(id=file_id)
    file_path = file.file
    file_column = file.column
    try:
        process_file_data(file_path=file_path, name_column=file_column)
        file.is_processed = True
        file.processed_at = datetime.now()
        await file.save()
        return True
    except Exception as ex:
        print(ex)
        return False
    # list_hubs = Hub.objects.all().values('hub_name', 'hub_link')
    # pars = ParserHub()
    # pars(celery_task_id=self.request.id, list_hubs=list_hubs)
    # return True
