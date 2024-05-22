from pydantic import BaseModel


class File(BaseModel):
    file_uuid: str
    file_name: str
    is_processed: bool
    process_status: bool
    created_at: float
