from src.pipeline.data_ingestion_pipeline import DataIngestionTraining
from src.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.pipeline.data_validation_pipeline import DataValidator
from src.pipeline.model_training_pipeline import ModelTrainerPipeline
from src.logger import logging
from src.exception import CustomException


# STAGE_NAME = "Data Ingestion"
# try:
#     logging.info(f"--------------------{STAGE_NAME} start--------------------")
#     obj = DataIngestionTraining()
#     ingest_data_path = obj.main()
#     logging.info(f"------------------------{STAGE_NAME} end--------------------")
# except Exception as e:
#     raise e


# STAGE_NAME = "Data Transformation"
# try:
#     logging.info(f"--------------------{STAGE_NAME} start--------------------")
#     obj = DataTransformationPipeline(ingest_data_path)
#     cleaned_text_path = obj.main()
#     logging.info(f"------------------------{STAGE_NAME} end--------------------")
# except Exception as e:
#     raise e


# STAGE_NAME = "Data Validation"
# try:
#     logging.info(f"--------------------{STAGE_NAME} start--------------------")
#     obj = DataValidator(cleaned_text_path)
#     obj.main()
#     logging.info(f"------------------------{STAGE_NAME} end--------------------")
# except Exception as e:
#     raise e
#cleaned_text_path[0], cleaned_text_path[1]

STAGE_NAME = "Model Trainer"
try:
    logging.info(f"--------------------{STAGE_NAME} start--------------------")
    obj = ModelTrainerPipeline('artifacts/data_transformation/train_texts.csv', 'artifacts/data_transformation/validation_texts.csv')
    obj.main()
    logging.info(f"------------------------{STAGE_NAME} end--------------------")
except Exception as e:
    raise e