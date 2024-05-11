from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFileRequest(_message.Message):
    __slots__ = ("filename", "file", "updated_at", "created_at")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    filename: str
    file: bytes
    updated_at: float
    created_at: float
    def __init__(self, filename: _Optional[str] = ..., file: _Optional[bytes] = ..., updated_at: _Optional[float] = ..., created_at: _Optional[float] = ...) -> None: ...

class CreateFileResponse(_message.Message):
    __slots__ = ("file_uuid",)
    FILE_UUID_FIELD_NUMBER: _ClassVar[int]
    file_uuid: str
    def __init__(self, file_uuid: _Optional[str] = ...) -> None: ...

class GetFileRequest(_message.Message):
    __slots__ = ("file_uuid",)
    FILE_UUID_FIELD_NUMBER: _ClassVar[int]
    file_uuid: str
    def __init__(self, file_uuid: _Optional[str] = ...) -> None: ...

class GetFileResponse(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...
