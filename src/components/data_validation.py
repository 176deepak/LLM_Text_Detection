import os
import sys
from pathlib import Path
from src.logger import logging
from src.exception import CustomException
from src.entity import DataValidationConfig

class DataValidation:
    def __init__(self, files, config: DataValidationConfig):
        self.files = files
        self.config = config


    def validate_files(self):
        validation_status = None

        try:
            data_files = [file.split("/")[-1] for file in self.files]
            for data_file in data_files:
                if data_file not in self.config.required_files:
                    validation_status = False
                    with open(self.config.status_filepath, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                    break
                else:
                    validation_status = True
                    with open(self.config.status_filepath, 'w')   as f:
                        f.write(f"Validation status: {validation_status}")

            if validation_status == True:
                logging.info(f"All required files are present.")
            else:
                logging.info(f"All required files are not present.")
            return validation_status

        except Exception as e:
            raise CustomException(e, sys)
        