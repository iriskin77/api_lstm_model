from abc import abstractmethod, ABC
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Generic, Type, TypeVar, Union, Sequence
from pydantic import BaseModel


class BaseRepository(ABC):

    @abstractmethod
    def get(self):
        raise NotImplementedError

    @abstractmethod
    def create(self):
        raise NotImplementedError

    @abstractmethod
    def put(self):
        raise NotImplementedError

    @abstractmethod
    def patch(self):
        raise NotImplementedError


ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class FileRepository(BaseRepository, Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, client_minio: Type[ModelType]):
        self._client = client_minio

    async def get(self):
        pass

    async def create(self):
        pass

    async def put(self):
        pass

    async def patch(self):
        pass


# initialize repository

