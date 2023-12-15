# Import required modules
from src.logger import logging
from src.exception import CustomException
from src.config import configuration
from src.components.data_transformation import DataTransformation


# Class definition for DataTranformation pipeline
class DataTransformationPipeline:
    def __init__(self, raw_data_path):
        self.raw_data_path = raw_data_path

    
    def main(self):
        config = configuration.ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(self.raw_data_path, data_transformation_config)
        data_transformation.transform_text()
        return data_transformation_config.cleaned_text_file

