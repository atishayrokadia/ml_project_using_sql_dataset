from src.mlProject.components.data_ingestion import DataIngestion
from src.mlProject.components.data_ingestion import DataIngestionConfig
from src.mlProject.logger import logging
from src.mlProject.exception import CustomException
import sys

if __name__=='__main__':
    logging.info("The execution has started")

    try:
        # data_ingection_config =  DataIngestionConfig()
        data_ingestion =  DataIngestion()
        data_ingestion.initiate_data_ingestion()  

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)