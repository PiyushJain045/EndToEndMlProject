# Data Ingestion is the process of collecting, importing, and processing raw data from various sources into a storage system 
# (like a database, data warehouse, or data lake) for further analysis or machine learning.

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

# Define the DataIngestionConfig class using the dataclass decorator
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


# Define the DataIngestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # read data
            print("DEBUG")
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as dataframe')

            # make artifact directory --> stores train, test, raw (data)
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path) ,exist_ok=True )

            # 1)raw data csv
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train test split initiated")
            
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            #2) train data csv
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            #3) test data csv
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)



# Main block. For testing when runned directly
if __name__ == "__main__":
    # file 1 data_ingestion.py
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    # Print the ingestion configuration
    print("Answer:", train_data)

   # file 2 data_transformation.py
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

   # file 3 model_trainer.py











