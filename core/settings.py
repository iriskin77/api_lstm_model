import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, ".env"))

PATH_FILE_STORAGE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "file_storage/")


DATABASE_URI = f'postgres://{os.environ.get("POSTGRES_USER")}:' \
               f'{os.environ.get("POSTGRES_PASSWORD")}@' \
               f'{os.environ.get("POSTGRES_HOST")}:{os.environ.get("POSTGRES_PORT")}/' \
               f'{os.environ.get("POSTGRES_DB")}'


APPS_MODELS = [
    "models.models",
    "aerich.models",
]
#
# print(PATH_FILE_STORAGE)
# print(os.path.isdir(PATH_FILE_STORAGE))
# print(os.mkdir(PATH_FILE_STORAGE))
