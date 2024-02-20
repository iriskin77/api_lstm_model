from pydantic import BaseModel, FilePath
from datetime import datetime


class FileGet(BaseModel):

    id: int
    column: str
    file: str
    status: bool | None = None
    time_get: datetime | None = None


class FilePost(BaseModel):

    id: int
    name: str
    column: str
    file: str
    time_get: datetime | None = None
