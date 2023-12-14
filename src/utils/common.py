# Import necessary libraries
import os
import sys
import yaml
import pandas as pd
from pathlib import Path
from box import ConfigBox
import pymongo as mongo
from src.logger import logging
from src.exception import CustomException
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


# Function to read a config yaml files 
def read_yaml(path):
    # trying to open a file
    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path} loaded successfully")
            # return the content of the file
            return ConfigBox(content)
    except Exception as e:
        raise e
    

# Function to create directories 
def create_dirs(paths:list):
    for path in paths:
        path = Path(path)
        os.makedirs(path, exist_ok=True)
        logging.info(f"Created directory at {path}")


# Function to establish a MongoDB connection
def db_conn():
    try:
        # Get MongoDB connection details from environment variables
        host = os.getenv("host")
        port = os.getenv("port")
        print(host, port)
        # Create the connection string
        connection_str = f"mongodb://{host}:{port}"
        # Establish the MongoDB client connection
        client = mongo.MongoClient(connection_str)
        # Log successful database connection
        logging.info("database connection established successfully...")
        return client
    except Exception as e:
        # Raise a custom exception if there's an error during connection
        raise CustomException(e, sys)


# Function to retrieve data from a MongoDB collection and convert it to a Pandas DataFrame
def get_data(coll_name):
    try:
        # Connect to the database
        client = db_conn()
        # Get the database name from environment variables
        database = os.getenv("database")
        # Access the specified database
        db = client[database]
        # Access the specified collection within the database
        coll_df = db[coll_name]
        # Retrieve data from the collection and convert it to a DataFrame
        data = list(coll_df.find())
        df = pd.DataFrame(data, index=None)
        # Drop the '_id' column from the DataFrame
        df.drop(['_id'], axis=1, inplace=True)
        # Log successful conversion of collection to DataFrame
        logging.info(f"{coll_name} collection converted into dataframe successfully.")
        return df
    except Exception as e:
        # Raise a custom exception if there's an error during data retrieval or conversion
        raise CustomException(e, sys)
