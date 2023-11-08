## In this file we write the code about Data Read & train_test_split

import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


## intialize the data ingestion configuration
## (In this Class the ingestion class parameter means i read the data & train & 
## test the data i want to save this data to save data the specific path is defined here.)

@dataclass
class DataIngestionconfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')


## create a data ingestion class
## (It is Responsiable for Read the data & train test split of the data)

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig() # Here in The ingestion_config variable all the data path is come means train_data_path,test_data_path,raw_data_path is present in this variable.

    def initiate_data_ingestion(self):   # In this function we write all the main code this means read the data,train_test_split of the data & save the data
        logging.info('Data Ingestion method starts')

        try:
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))   # Read the Data from path
            logging.info('Dataset Read as Pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)  # Make the directory for raw data if present then simply exist_ok=True

            df.to_csv(self.ingestion_config.raw_data_path,index=False)  # To save the raw data index=False means index column is not present in my raw data

            logging.info("Train Test Split")
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)  # Split the data into two set train_set & test_set

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)  # Save the train_set data in the given path & header=True means Column name is present in train_set data
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)  # Save the test_set data in the given path & header=True means Column name is present in test_set data

            logging.info('Ingestion of Data is Completed')

            return(
                self.ingestion_config.train_data_path,  # This two value is required for next step in data_transformation.py file for feature engineering purpose
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            logging.info('Error Occured in Data Ingestion Config')