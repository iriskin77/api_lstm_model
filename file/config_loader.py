import os
from configloader import ConfigLoader

# Путь к файлу с конфигами (config.yml)
config_abs_path = "/".join(os.path.abspath(__file__).split('/')[0:-1])


class Config:
    def __init__(self, config_file_path=f'{config_abs_path}/config.yml'):
        # Загружаются переменные из config.yml
        self.config_loader = ConfigLoader()
        self.config_loader.update_from_yaml_file(config_file_path)
        self.config_loader.update_from_env_namespace('METRICS_COLLECTOR')

    def get(self, setting_name):
        # Для получения конкретной переменной из config.yml
        return self.config_loader.get(setting_name, None)

    def to_dict(self):
        loader = self.config_loader
        return {key: loader.get(key) for key in loader.keys()}

# Это переменные из config.yml

LOGGING_LEVEL = "LOGGING_LEVEL"
LOGGING_FORMAT = "LOGGING_FORMAT"
WEB_HOST = "WEB_HOST"
WEB_PORT = "WEB_PORT"
