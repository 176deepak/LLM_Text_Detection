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


@dataclass(frozen=True)
class DataTransformationConfig:
    cleaned_data_dir: Path
    cleaned_text_file: Path
    train_text_file: Path
    test_text_file: Path
    valid_text_file: Path


@dataclass
class DataValidationConfig:
    validation_dir: Path
    status_filepath: Path
    required_files: list


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    trained_model_dir: Path
    random_seed: int
    model_ckpt: str
    num_labels: int
    learning_rate: float
    num_train_epochs: int
    train_batch_size: int
    num_warmup_steps: int
    
    

# @dataclass(frozen=True)
# class ModelEvaluationConfig:
#     root_dir: Path
#     data_path: Path
#     model_path: Path
#     tokenizer_path: Path
#     metric_file_name: Path