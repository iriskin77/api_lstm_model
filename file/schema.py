from pydantic import BaseModel, FilePath, ConfigDict
from typing import Optional
from datetime import datetime


class FileGet(BaseModel):

    id: int
    filename: str
    column: str
    file: str
    is_processed: bool | None = None
    processed_at: datetime | None = None
    created_at: datetime | None = None


class FilePost(BaseModel):

    id: int | None = None
    name: str | None = None
    column: str | None = None
    file: str | None = None
    time_get: datetime | None = None

    model_config = ConfigDict(from_attributes=False, populate_by_name=True)


class FileUpdate(BaseModel):

    filename: str
    column: str


class FileFilter(BaseModel):

    filename: Optional[str] = None
    column: Optional[str] = None
    is_processed: Optional[bool] = None
