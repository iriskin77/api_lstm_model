import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


#DATABASE_URL_POSTGRES = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

DATABASE_URL_SQLITE = f"sqlite+aiosqlite:///file_db.sqlite3"

engine = create_async_engine(DATABASE_URL_SQLITE, echo=True, future=True)
SessionLocal = sessionmaker(autoflush=False, bind=engine, class_=AsyncSession)

path_file_storage = os.path.join(os.path.dirname(os.path.dirname(__file__)), "file_storage/files/")


url_api_currency = "https://www.cbr-xml-daily.ru/daily_json.js"
