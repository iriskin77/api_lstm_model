import os
from dotenv import load_dotenv
from pathlib import Path

#DATABASE_URL_POSTGRES = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

#DATABASE_URL_SQLITE = f"sqlite+aiosqlite:///file_db.sqlite3"

BASE_DIR = Path(__file__).resolve().parent.parent
#BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, ".env"))

#path_file_storage = os.path.join(os.path.dirname(os.path.dirname(__file__)), "file_storage/files/")


#url_api_currency = "https://www.cbr-xml-daily.ru/daily_json.js"


DATABASE_URI = f'postgres://{os.environ.get("POSTGRES_USER")}:' \
               f'{os.environ.get("POSTGRES_PASSWORD")}@' \
               f'{os.environ.get("POSTGRES_HOST")}:{os.environ.get("POSTGRES_PORT")}/' \
               f'{os.environ.get("POSTGRES_DB")}'


print(DATABASE_URI)

APPS_MODELS = [
    "models.models",
    "aerich.models",
]
