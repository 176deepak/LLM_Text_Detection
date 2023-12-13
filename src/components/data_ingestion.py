import os
from src.logger import logging
from src.entity import DataIngestionConfig
from src.books_recommender.utils.common import get_data
from dotenv import load_dotenv

load_dotenv()

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        books_df = get_data(coll_name=os.getenv("collection"))

        os.makedirs("data", exist_ok=True)
        books_df.to_csv(os.path.join("data", "data.csv"), index=False)
        logging.info(f"books data saved successfully at {self.config.books_data_file}")