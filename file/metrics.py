from prometheus_client import Counter
GET_FILE = Counter("get_file", "Count of get file")
UPLOAD_FILE = Counter("upload_file", "Count of upload file")
