from core.base import Base
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Boolean, Date


class FileUpload(Base):

    __tablename__ = "fileupload"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False, default=None)
    column = Column(String, nullable=False)
    file = Column(String, nullable=False, default=None)
    status = Column(Boolean, nullable=True, default=None)
    time_get = Column(DateTime)


# os.makedirs("./upload_dir/attachment", 0o777, exist_ok=True)
# container = LocalStorageDriver("./upload_dir").get_container("attachment")
# StorageManager.add_storage("default", container)
