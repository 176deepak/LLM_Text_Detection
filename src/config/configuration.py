from src.constants import *
from src.entity import *
from src.utils.common import read_yaml, create_dirs


class configurationManager:
    def __init__(self, config_filepath = CONFIG_YAML_FILE):
        self.config = read_yaml(config_filepath)
        create_dirs([self.config.artifacts_dir])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_dirs([config.ingestion_dir])

        data_ingestion_config = DataIngestionConfig(
            data_dir = config.ingestion_dir,
            text_data_file = config.data_file
        )

        return data_ingestion_config