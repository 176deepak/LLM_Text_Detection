# Import necessary modules
from pathlib import Path
from dataclasses import dataclass

# Define a data class for DataIngestion configuration
@dataclass(frozen=True)
class DataIngestionConfig:
    # Path to the directory where data will be stored
    data_dir: Path
    # Path to the file containing text data within the specified data directory
    text_data_file: Path



# @dataclass(frozen=True)
# class DataTransformationConfig:
#     root_dir: Path
#     data_path: Path
#     tokenizer_name: Path


# @dataclass(frozen=True)
# class ModelTrainerConfig:
#     root_dir: Path
#     data_path: Path
#     model_ckpt: Path
#     learning_rate: float
#     num_train_epochs: int
#     per_device_train_batch_size: int
#     weight_decay: float
#     evaluation_strategy: str
    

# @dataclass(frozen=True)
# class ModelEvaluationConfig:
#     root_dir: Path
#     data_path: Path
#     model_path: Path
#     tokenizer_path: Path
#     metric_file_name: Path