from src.config import configuration
from src.components.model_training import ModelTrainer


class ModelTrainerPipeline:
    def __init__(self, train_data_path, valid_data_path):
        self.train_data_path = train_data_path
        self.valid_data_path = valid_data_path

    
    def main(self):
        config = configuration.ConfigurationManager()
        model_training_config = config.get_model_training_config()
        trainer = ModelTrainer(self.train_data_path, self.valid_data_path, model_training_config)
        trainer.train_model()