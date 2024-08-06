import os
import sys
from src.mlProject.exception import CustomException
from src.mlProject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("reading sql database")

    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("connection estabilished")
        df = pd.read_sql_query('Select * from student',mydb)

        return df
    except Exception as  e:
        raise CustomException(e,sys)
    
    
    