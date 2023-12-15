from src.config import configuration
from src.components import model_training


class ModelTrainerPipeline:
    def __init__(self, cleaned_text_path):
        self.clean_text_path = cleaned_text_path

    
    def main(self):
        config = configuration.ConfigurationManager()
        model_training_config = config.get_model_training_config()
