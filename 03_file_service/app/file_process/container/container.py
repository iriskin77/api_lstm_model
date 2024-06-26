from app.file_process.repository.repository import FileRepository, repo
from app.file_process.core.use_cases.services import FileService
from dependency_injector import containers, providers


class Container:

    def __init__(self, file_repo: FileRepository):
        self._file_repo = file_repo

    def get_file_service(self) -> FileService:
        return FileService(self._file_repo)


container = Container(repo)
