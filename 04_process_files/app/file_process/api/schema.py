from pydantic import BaseModel


class FileCreateDTO(BaseModel):
    file_name: str
    file_path: str
