# Importing necessary modules and entities from the src package
from src.constants import *
from src.entity import *
from src.utils.common import read_yaml, create_dirs


# Class definition for ConfigurationManager
class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_YAML_FILE):
        # Constructor to initialize the instance with the specified configuration file path
        self.config = read_yaml(config_filepath)        
        # Create necessary directories based on the configuration
        create_dirs([self.config.artifacts_dir])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Retrieve data ingestion configuration from the overall configuration
        config = self.config.data_ingestion
        # Create directories specified in the data ingestion configuration
        create_dirs([config.ingestion_dir])
        # Instantiate DataIngestionConfig with relevant parameters
        data_ingestion_config = DataIngestionConfig(
            data_dir=config.ingestion_dir,
            text_data_file=config.data_file
        )
        # Return the instantiated DataIngestionConfig object
        return data_ingestion_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        # Retrieve data transformation configuration from the overall configuration
        config = self.config.data_transformation
        # Create directories specified in the data transformation configuration
        create_dirs([config.transformation_dir])
        # Instantiate DataTransformationConfig with relevant parameters
        data_transformation_config = DataTransformationConfig(
            cleaned_data_dir=config.transformation_dir,
            cleaned_text_file=config.cleaned_data_dir
        )
        # Return the instantiated DataTransformationConfig object
        return data_transformation_config
