from src.constants import *
from src.entity import *
from src.utils.common import read_yaml, create_dirs


class configurationManager:
    def __init__(self, config_filepath = CONFIG_YAML_FILE):
        self.config = read_yaml(config_filepath)
        create_dirs([self.config.artifacts_dir])
