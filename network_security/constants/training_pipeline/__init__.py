import os
import sys
import numpy as np
import pandas as pd

'''
Defining comman constant variable for training pipeline
'''
TARGET_COLUMN = "Result" 
PIPLINE_NAME = "NetworkSecurity" 
ARTIFACT_DIR = "Artifacts" 
FILE_NAME = "phisingData.csv" 

TRAIN_FILE_NAME = "train.csv" 
TEST_FILE_NAME = "test.csv" 


'''
Data Ingestion related constants start with DATA_INGESTION VAR NAME
'''

DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "Megh"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str =  "feature_score"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2
