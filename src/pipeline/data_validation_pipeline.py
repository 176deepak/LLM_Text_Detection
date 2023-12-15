from src.config import configuration
from src.components.data_validation import DataValidation
from src.logger import logging

class DataValidator:
    def __init__(self, text_files):
        self.files = text_files

    def main(self):
        config = configuration.ConfigurationManager()
        data_ingestion_config = config.get_data_validation_config()
        validatior = DataValidation(self.files, data_ingestion_config)
        validatior.validate_files()