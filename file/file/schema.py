from pydantic import BaseModel, FilePath, ConfigDict
from datetime import datetime


class FileGet(BaseModel):

    id: int
    column: str
    file: str
    status: bool | None = None
    time_get: datetime | None = None


class FilePost(BaseModel):

    id: int | None = None
    name: str | None = None
    column: str | None = None
    file: str | None = None
    time_get: datetime | None = None

    model_config = ConfigDict(from_attributes=False, populate_by_name=True)
