import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion

from src.components.data_transformation import DataTransformation

from src.components.model_trainer import ModelTrainer


if __name__=='__main__':
    obj = DataIngestion()   # When we initilize this here come the 3 file path of data_ingestion file train_data_path,test_data_path,raw_data_path by executing __init__ function in DataIngestion class
    train_data_path,test_data_path=obj.initiate_data_ingestion()  # initiate_data_ingestion() initilize this function from data_ingestion.py file
    print(train_data_path,test_data_path)

    data_transformation = DataTransformation()   # Create the Object of DataTransformation() class from data_transformation.py file

    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)   # Data transformation is done and the pickel file is saved & the transformation train & test data is ready for model training

    model_trainer = ModelTrainer()    # Initilize ModelTrainer class from model_trainer.py file
    model_trainer.initate_model_training(train_arr,test_arr)   # Train & Test data are train by using this function