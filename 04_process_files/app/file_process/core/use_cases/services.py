from abc import abstractmethod, ABC


class BaseService(ABC):

    @abstractmethod
    def get_user_by_id(self, user_id: int):
        raise NotImplementedError

    @abstractmethod
    def create_user(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    def update_user(self, data: dict):
        raise NotImplementedError


class FileService(BaseService):

    def __init__(self, repo):
        self._repo = repo

    def get_user_by_id(self, user_id: int):
        pass

    def create_user(self, data: dict):
        pass

    def update_user(self, data: dict):
        pass
