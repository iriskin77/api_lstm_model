import os
import json
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR_ENV = Path(__file__)
#load_dotenv(os.path.join(BASE_DIR, ".env"))


BASE_DIR = Path(__file__).resolve().parent.parent

#print(str(BASE_DIR) + "/apps/file/file_storage")
load_dotenv(os.path.join(BASE_DIR, ".env"))
#absolute_path = os.path.abspath('file/apps')

#PATH_FILE_STORAGE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "apps/file/file_storage")
PATH_FILE_STORAGE = str(BASE_DIR) + "/apps/file/file_storage/"



DATABASE_URI = f'postgres://{os.environ.get("POSTGRES_USER")}:' \
               f'{os.environ.get("POSTGRES_PASSWORD")}@' \
               f'{os.environ.get("POSTGRES_HOST")}:{os.environ.get("POSTGRES_PORT")}/' \
               f'{os.environ.get("POSTGRES_DB")}'


APPS_MODELS = [
    "file.models",
    "user.users.models",
    "aerich.models",
]

SECRET_KEY: str = "secret_key"
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

print(BASE_DIR_ENV)
print(os.environ.get("POSTGRES_PORT"))


# abs_path = Path(__file__).resolve().parent.parent
#
# model = load_model(rf"{abs_path}/model/best_model_LSTM10000_2.h5")
#
# with open(rf'{abs_path}/model/tokenizer_json.json') as file:
#     data = json.load(file)
#     tokenizer = tokenizer_from_json(data)
