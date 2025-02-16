import os
import sys
from src.mlProject.exception import CustomException
from src.mlProject.logger import logging
import pandas as pd
from src.mlProject.utils import read_sql_data
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifact','train.csv')
    test_data_path = os.path.join('artifact','test.csv')
    raw_data_path = os.path.join('artifact','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config =  DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            df = read_sql_data()
            logging.info('Reading mysql database')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            print(type(df),"##################################################")
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            df.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            df.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Data Ingestion is completed you can see artifact folder')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                )
        except Exception as  e:
            logging.info("Custom exception")
            raise CustomException(e,sys)